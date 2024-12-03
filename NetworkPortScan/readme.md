Multithreaded Port Scanner
This project is a Python-based multithreaded port scanner that checks for open ports on a given IP address within a user-specified range. It leverages threading for faster scanning and provides a user-friendly summary of the results.

Features
Validates user input for IP address and port range.
Uses multithreading for efficient scanning.
Handles errors gracefully to avoid interruptions.
Provides a summary of open ports at the end of the scan.

Requirements
To run this script, ensure you have:
Python 3.7 or later installed.

Installation
Clone the repository:
git clone https://github.com/ITASMDY/ITAS.git
cd your-repo

Usage
Run the script:
python networkPortScan.py

Input the required information when prompted:
IP Address: Enter a valid IPv4 address (e.g., 192.168.1.1).
Start Port: The first port in the range to scan (e.g., 20).
End Port: The last port in the range to scan (e.g., 100).

Validate your inputs.
Scan the specified range of ports on the provided IP address.
Display open ports in real time.
Provide a summary of open ports at the end.
