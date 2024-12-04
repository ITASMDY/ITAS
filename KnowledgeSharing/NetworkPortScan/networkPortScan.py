import socket
import ipaddress
import threading


#Requesting User Input for IP, Start Port and Endport
ip = input("Enter IP addres:")
start_port = int(input("Enter the start port:"))
end_port = int(input("Enter the end port:"))

# Define a function to scan a IP and port
def scan_port(ip,start_port,end_port):
    for port in range(start_port,end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Timeout for faster scanning
                result = s.connect_ex((ip, port))  # Returns 0 if port is open
                if result == 0:
                    print(f"Port {port} is open on {ip}")             
        except Exception as e:
            print(f"Error scanning port {port} on {ip}: {e}") # Handle errors appropriately
  
scan_port(ip, start_port, end_port)
    

