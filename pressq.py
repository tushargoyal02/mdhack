#!/usr/bin/python2
import time 
import os 
print "press 1 to check current time :"
print "press 2 :"
print "press 3  open browser :"
print "press 6 to check all the network ip : "
ch=raw_input()

if ch == '1'   : 

    print time.ctime()

elif ch == '2'  : 
    print "two"

if ch ==  '3' :

    print firefox()

elif ch == '6' : 

    print  nmap -sP -n -T5 192.168.10.0/24 | grep -i 192 
else : 
       print "no chance!!" 
