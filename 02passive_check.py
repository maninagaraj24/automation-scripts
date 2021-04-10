#!/usr/bin/python
import os
#import socket
#ip = ('{0}'.format(socket.gethostbyname(socket.gethostname())))
#socket.gethostbyname(socket.gethostname())
service_data = ["postman", "CRN status", "VerifyMPIN", "CCList", "AccList"]

for i in service_data:
        ser = ('localhost'+ ';' + i + ';' + '0' + ';' +'OK' )
        #print(ser)
cmd= 'echo ' + ser    
os.system( cmd  "|  /opt/nagios/bin/send_nsca 192.168.2.191 -d ; -c /etc/nagios/send_nsca.cfg")

for i in service_data:
        ser = (ip+ ';' + i + ';' + code + ';' + status)
        try:
            #sp=subprocess.run([cmd, ser, '|', '/opt/nagios/bin/send_nsca -H 192.168.2.191 -d', ';',' -c /etc/nagios/send_nsca.cfg'],check=True)
           # subprocess.run([' echo', "{0};{1};{2};{3}".format(ip, i, code, status),],check=True)
           # subprocess.run([ '/opt/nagios/bin/send_nsca -H 192.168.2.191 -d ; -c /etc/nagios/send_nsca.cfg'],check=True)
            nsca=subprocess.run(['echo', send, '|', '/opt/nagios/bin/send_nsca', '-H', '192.168.2.191', '-d', ';', '-c', '/etc/nagios/send_nsca.cfg'],shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
       #     sp=subprocess.Popen([cmd],stdin=nsca.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
       #     nsca.stdout.close()
           # output = nsca.communicate()[0]
            print(nsca)

        except subprocess.CalledProcessError as e:
            e.returncode
