#!/usr/bin/env python

import os

os.system("apt-get install figlet")

os.system("clear")

os.system("figlet Port Scanner")

print("""


1) Fast Scan
2) Information of the service and version
3) Infortmation of Operating System

""")

process_no = input("Enter process number : " )

if(process_no=="1"):

	target_ip = input("Target Ip : ")

	os.system("nmap " + target_ip)

elif(process_no=="2"):

	target_ip = input("Target Ip : " )

	os.system("nmap -sS -sV " + target_ip)
	
elif(process_no=="3"):

	target_ip = input("Target Ip : ")
	
	os.system("nmap " + target_ip)





