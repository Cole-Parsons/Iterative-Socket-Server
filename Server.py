#VPN IP: 10.0.96.62

import socket 
import subprocess

def send_date_time(sock):
    result = subprocess.run(['date'], capture_output=True, text=True)
    date_time = result.stdout
    sock.sendall(date_time.encode())

def send_uptime(sock):
    result = subprocess.run(['uptime'], capture_output=True, text=True)
    output = result.stdout.strip()

    words = output.split('up')[1]
    words = words.split(',')
    uptime_only = ','.join(words[:2])

    sock.sendall(uptime_only.encode())

def send_memory_use(sock):
    result = subprocess.run(['free', '-h'], capture_output=True, text=True)
    memory_line = result.stdout.splitlines()[1]

    sock.sendall(memory_line.encode())

def send_netstats(sock):
    result = subprocess.run(['ss', '-tuln'], capture_output=True, text=True)
    netstat_lines = result.stdout.splitlines()[1:]
    netstat_string = '\n'.join(netstat_lines)

    sock.sendall(netstat_string.encode())

def send_running_processes(sock):
    result = subprocess.run(['ps', '-e'], capture_output=True, text=True)
    running_processes = result.stdout.splitlines()[1:]
    running_processes_string = '\n'.join(running_processes)

    sock.sendall(running_processes_string.encode())

print('Starting Iterative Socket Server...')
port = input('Port: ')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', int(port)))
server.listen()

while True:
    conn, addr = server.accept()
    client_command = conn.recv(1024).decode().strip().lower()

    if client_command == 'date and time':
        send_date_time(conn)
    elif client_command == 'uptime':
        send_uptime(conn)
    elif client_command == 'memory use':
        send_memory_use(conn)
    elif client_command == 'netstats':
        send_netstats(conn)
    elif client_command == 'running processes':
        send_running_processes(conn)
    else:
        conn.sendall('Invalid option'.encode())
    
    conn.close()