#!/usr/bin/python

import socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto("MDhack",("192.168.10.177",9999)) 
