# !/usr/bin/python3
# -*- coding:utf-8 -*-
# _*_ coding:cp1254 _*_
#Ahmed Demirezen
import socket
import time



while True:
    try:
        #Server İnformation
        server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host="localhost"
        port=6969
        buf=1024

        server.connect((host,port))

        while True:
            data=server.recv(buf)
            if data=="command".encode():
                print("Connection is succesfully")
        #Vertical
            elif data=="V 0".encode():
                print("V 0")
            elif data=="V 1".encode():
                print("V 1")
            elif data=="V 2".encode():
                print("V 2")
            elif data=="V 3".encode():
                print("V 3")
            elif data=="V 4".encode():
                print("V 4")
            elif data=="V 5".encode():
                print("V 5")
            elif data=="V 6".encode():
                print("V 6")
            elif data=="V 7".encode():
                print("V 7")
            elif data=="V 8".encode():
                print("V 8")
            elif data=="V 9".encode():
                print("V 9")
            elif data=="V 10".encode():
                print("V 10")
        #Horizontal
            elif data=="H 0".encode():
                print("H 0")
            elif data=="H 1".encode():
                print("H 1")
            elif data=="H 2".encode():
                print("H 2")
            elif data=="H 3".encode():
                print("H 3")
            elif data=="H 4".encode():
                print("H 4")
            elif data=="H 5".encode():
                print("H 5")
            elif data=="H 6".encode():
                print("H 6")
            elif data=="H 7".encode():
                print("H 7")
            elif data=="H 8".encode():
                print("H 8")
            elif data=="H 9".encode():
                print("H 9")
            elif data=="H 10".encode():
                print("H 10")        
        #Other        
            elif data=="close".encode():
                print("client shutting down")
                break
            
            elif data=="laser0".encode():
                print("laser is off")
                
            elif data=="laser1".encode():
                print("laser is on")
                

        server.close()
        
    except ConnectionRefusedError:
        print("connection is ineffective. restarting client please wait,ErrorCode: ConnectionRefusedError")
    except ConnectionResetError:
        print("connection is ineffective. restarting client please wait,ErrorCode: ConnectionResetError")
        
