#!/usr/bin/env python
__author__ = 'skunda'

import serial
import httplib, urllib
import time
import string


ser=serial.Serial('/dev/ttyUSB0', 9600)


#sleep = 1 # how many seconds to sleep between posts to the channel
key ="GF1QZWAA0819JA8M"  # Thingspeak channel to update



def thermometer():
    while True: 

        #node1x=0
        #node1y=0

        #node2x=0
        #node2y=0

        #node3x=0
        #node3y=0

        #node4x=0
        #node4y=0

        string=ser.readline()
        #print(string)
        nodeNumber=string.split(" ")[0]
        #X=string.split(" ")[1]
        #Y=string.split(" ")[2]

        if nodeNumber=="1":
            node1x=string.split(" ")[1]
            node1y=string.split(" ")[2]
            params = urllib.urlencode({'field1': node1x, 'field2':node1y , 'key':key})
            #print(nodeNumber)
            #print(node1x)
            #print(node1y)
        if nodeNumber=="2":
            node2x=string.split(" ")[1]
            node2y=string.split(" ")[2]
            params = urllib.urlencode({'field3':node2x , 'field4':node2y , 'key':key})
        if nodeNumber=="3":
            node3x=string.split(" ")[1]
            node3y=string.split(" ")[2]
            params = urllib.urlencode({'field5':node3x , 'field6':node3y , 'key':key})
        if nodeNumber=="4":
            node4x=string.split(" ")[1]
            node4y=string.split(" ")[2]
            params = urllib.urlencode({'field7':node4x , 'field8':node4y , 'key':key})
            #print(nodeNumber)
            #print(node4x)
            #print(node4y)

        

        
        #params = urllib.urlencode({'field1': node1x, 'field2':node1y , 'field3':node2x , 'field4':node2y , 'field5':node3x , 'field6':node3y , 'field7':node4x , 'field8':node4y , 'key':key})
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("140.127.194.107:3000")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            conn.close()
        except:
            print ("connection failed")
        break
#sleep for desired amount of time
if __name__ == "__main__":
        while True:
                thermometer()
                #time.sleep(1)
