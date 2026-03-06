#VPN IP: 10.0.96.62

import socket 
import subprocess

def send_date_and_time(sock):
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



print('Starting Iterative Socket Server...')
port = input('Port: ')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', int(port)))
server.listen()

send_uptime()



