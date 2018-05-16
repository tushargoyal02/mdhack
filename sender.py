#!/usr/bin/python2

import socket 
sender_ip="192.168.10.177"
myport=9999
#                     IPV4, for udp 
# only for reciver 
# for tcp dgram hatake stream in caps
# below ,ethod wth argument creating a soket  called s 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# now conenctng ip and port 

s.bind((sender_ip,myport))

