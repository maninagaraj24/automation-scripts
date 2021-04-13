#!/bin/bash
ser="192.168.2.194 192.168.2.197 192.168.2.248"
ssh_ps="sshpass -p 1 ssh -n -o StrictHostKeyChecking=No -o PubkeyAuthentication=No infra"

for server in $ser
do
	echo -e "\nWelcome to Server $server\n"  >> server_details.csv
	Public_IP=$(curl ifconfig.io)
	Internal_IP=$(ifconfig | grep inet | awk 'NR==1{print $2}')
	OS_Details=$(hostnamectl  | awk -F " " 'NR==5{print $3,$4}')
	Kernal_Version=$(uname -r)
	Architecture=$(uname -a | awk '{print $12}')
	HDD=$(df -hTH / | awk 'NR==2{print $3}')
	CORE=$(lscpu | awk 'NR==4{print $2}')
	#CPU=$(lscpu | awk 'NR==10{print $2}')
	CPU=$(lscpu | grep "Model name"|awk -F ":" '{print $2}'| tr -d " ")
	MEMORY=$(free -g | awk 'NR==2{print $2}')
	Swap_MEMORY=$(free -g | awk 'NR==4{print $2}')
	Bash_Version=$(bash --version | awk -F " " 'NR==1{print $4}')

	echo -e "Public_IP,$Public_IP,\nInternal_IP,$Internal_IP,\nOS_Details,$OS_Details,\nKernal_Version,$Kernal_Version,\nArchitecture,$Architecture,\nHDD,$HDD,\nCORE,$CORE\nCPU,$CPU.\nMEMORY,$MEMORY,\nSwap_MEMORY,$Swap_MEMORY,\nBash_Version,$Bash_Version,\nMonit_Version,$monit" >> server_details.csv

done


