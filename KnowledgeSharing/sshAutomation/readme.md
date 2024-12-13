# SSH Automation Script

This script uses the Paramiko library to automate SSH connections to network devices, execute commands, and save the output to a log file.

## Features

- Connects to multiple devices via SSH.
- Executes commands on remote devices.
- Saves command output to a timestamped log file.
- Uses `paramiko` for SSH operations.

## Requirements

- Python 3.x
- `paramiko` library
- Network access to target devices.

## Installation

1. Clone this repository or download the script file.
2. Ensure Python 3.x is installed on your system.
3. Install the `paramiko` library:
   ```bash
   pip install paramiko
Usage
Edit the script to specify:

Username and Password in the un and pw variables.
Target device IP addresses in the netDev list.
Desired location for log files in the filLoc variable.
Run the script:

python script.py

The script will:

Connect to each device in the netDev list.
Execute the following commands:
ip addr
whomi
Save the output in a log file at the specified location.
File Output
The log files will be saved in the folder specified in filLoc. Each log file is named with a timestamp to differentiate between runs.

Notes
Ensure you have the necessary permissions and SSH access to the target devices.
Update the timeout parameter in the svrssh.connect() method as needed for your environment.
Customize the commands in the remote.send() method to suit your use case.