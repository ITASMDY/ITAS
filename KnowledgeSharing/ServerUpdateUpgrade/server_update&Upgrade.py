import paramiko
import time,os
username = input("Enter User Name: \n")
password = input("Enter Password: \n")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

filLoc = 'C:\\Scripts\\Log\\'
if not os.path.exists(filLoc):
    os.makedirs(filLoc)
    print(f"Folder '{filLoc}' created successfully.")

fName = os.path.join(filLoc, time.strftime("%Y%m%d-%H%M%S"))
srvIp = ["192.168.100.114","192.168.100.117"]
for ip in srvIp:
    try:
        ssh.connect(ip, port=22, username=username, password=password, timeout=10)
        print(f" Server {ip} is now connected!!!")
        remote = ssh.invoke_shell()
        remote.send("lsb_release -a \n")
        time.sleep(2)
        remote.send('sudo apt update\n')
        time.sleep(2)  
        remote.send(password + '\n')
        time.sleep(5)  
        remote.send('sudo apt upgrade -y \n')
        time.sleep(10) 
        output = remote.recv(65000).decode('utf-8')
        print(output)
        with open(f"{fName}_{ip}_sshlog.txt",'a') as f:
            f.write(output)
        print("Update and upgrade commands executed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ssh.close()
        