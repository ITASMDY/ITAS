# Automated Server Maintenance Script

This script automates SSH connections to servers for executing system update and upgrade commands using the `paramiko` library. It logs the output for each server in separate timestamped files.

## Features

- Connects to multiple servers via SSH.
- Executes Linux commands for system updates and upgrades.
- Logs the output of commands to timestamped files for each server.
- Ensures the log directory is created if it doesn't exist.

## Requirements

- Python 3.x
- `paramiko` library
- SSH access to the servers.

## Installation

1. Clone this repository or download the script.
2. Install the required Python library:
   ```bash
   pip install paramiko

Usage
Open the script and specify:

The list of server IP addresses in the srvIp variable.
The location for storing log files in the filLoc variable.
Run the script:

python script.py

The script will prompt you for your SSH username and password. Enter these credentials.

The script will:

Connect to each server in the srvIp list.
Execute the following commands:
lsb_release -a (fetch distribution information).
sudo apt update (update the package list).
sudo apt upgrade -y (upgrade installed packages).
Logs for each server are saved in the specified directory with filenames containing the server IP and timestamp.

File Output
Logs are stored in the directory specified by the filLoc variable. Each log file is named as:

<timestamp>_<server-ip>_sshlog.txt

Notes
Ensure the username has sufficient permissions to execute the sudo commands.
If the server requires confirmation for adding a host key, the script will automatically accept it.
Update the timeout parameter in the ssh.connect() method as needed.