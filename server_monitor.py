# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:13:18 2024

@author: Wai Phyo
"""

import paramiko
import time
import os
import getpass

#un = raw_input("Enter User Name: ")
#pw = getpass.getpass("Enter the Password:")
un = 'user'
pw = 'password'
filLoc = 'C:\\Scripts\\Log\\'
result = []
netDev = ['192.168.100.114']
#netDev = ['192.168.100.34','192.168.100.35','192.168.100.36','192.168.100.37','192.168.100.38']
fName = os.path.join(filLoc,time.strftime("%Y%m%d-%H%M%S"))

for ip in netDev:
	print(ip)
	svrssh = paramiko.SSHClient()
	svrssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	svrssh.connect(ip,port=22,username=un,password=pw,timeout=10)
	remote = svrssh.invoke_shell()
	remote.send('ip addr \n')
	time.sleep(1)
	remote.send('whomi')
	time.sleep(2)
    buf= remote.receive(65000)
	#print(buf.decode('utf-8'))
	f = open(fName + '_sshlog.txt','a')
	f.write(buf)
	f.close()
svrssh.close()

