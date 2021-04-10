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

