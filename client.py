import socket
import time
import threading

OPERATIONS = {
    "1": ("Date and Time", "date and time"),
    "2": ("Uptime", "uptime"),
    "3": ("Memory Use", "memory use"),
    "4": ("Netstat", "netstat"),
    "5": ("Current Users", "current users"),
    "6": ("Running Processes", "running processes")
}

def client_session(host, port, operation, results, index):
    start = time.time()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((host, port))
            s.sendall(operation.encode())

            response = b""
            while True:
                chunk = s.recv(4096)
                if not chunk:
                    break
                response += chunk

        end = time.time()
        elapsed = end - start
            
        results[index] =  (response.decode(), elapsed)

    except ConnectionRefusedError:
        print(f"   Client {index + 1}: Connection refused - is the server running?")
    except socket.timeout:
        print(f"   Client {index + 1}: Connection timed out - check the IP Address.")
    except Exception as e:
        print(f"   Client {index + 1}: Unexpected error - {e}")

def run_clients(host, port, operation, num_clients):

    threads = []
    results = [None] * num_clients
    
    for i in range(num_clients):
        t = threading.Thread(
            target=client_session,
            args=(host, port, operation, results, i)
        )
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return results

def get_valid_port():
    while True:
        try:
            port = int(input("Enter server port (1025-4998): ").strip())
            if 1025 <= port <= 4998:
                return port
            print("    Invalid port. Please enter a number between 1025 and 4998.")
        except ValueError:
            print("    Invalid input. Please enter a number")

def get_valid_host():
    while True:
        host = input("Enter server host: ").strip()
        if host == "":
            print("    Host cannot be empty.")
            continue
        try:
            socket.gethostbyname(host)
            return host
        except socket.gaierror:
            print(f"    Could not resolve host '{host}'. Please try again.")


def get_valid_operation():

    while True:
        operation = input("\nSelect Operation (1-6): ").strip()

        if operation in OPERATIONS:
            return operation

        print("    Invalid Choice. Please Enter a number between 1 and 6.")

def get_valid_num_clients():

    valid = [1,5,10,15,20,25]

    while True:
        try:
            num = int(input("Number of clients (1/5/10/15/20/25): ").strip())

            if num in valid:
                return num
            
            print(f"   Invalid choice. Please enter one of: {valid}")

        except ValueError:
            print("    Invalid input. Please enter a number.")

def main():
    print("=== Iterative Socket Server Client ===\n")

    host = get_valid_host()
    port = get_valid_port()

    print("\nAvailable Operations:")
    for key, value in OPERATIONS.items():
        print(f" {key}: {value}")

    operation = get_valid_operation()

    num_clients = get_valid_num_clients()

    print(f"\n--- Configuration ---")
    print(f"Host:       {host}")
    print(f"Port:       {port}")
    print(f"Operation:  {OPERATIONS[operation]}")
    print(f"Clients:    {num_clients}")

    print(f"\nSpawning {num_clients} client(s)...")
    results = run_clients(host, port, operation, num_clients)

    total = 0
    successful = 0
    print(f"\n--- Results ---")
    print(f"{'Client':<10} {'Turn-around Time'}")
    print("-" * 30)

    for i, result in enumerate(results):
        if result is None:
            print(f"   {i + 1}:<8 FAILED")
        else:
            response, elapsed = result
            print(f"    {i+1:<8} {elapsed*1000:.2f}ms")
            total += elapsed
            successful += 1
    
    average = total / num_clients

    if successful > 0:
        print("-" * 30)
        print(f"Total:      {total*1000:.4f}ms")
        print(f"Average:    {average*1000:.4f}ms")
        print(f"({successful}/{num_clients} clients succeeded)")
    else:
        print("No successful connections.")

if __name__ == "__main__":
    main()


