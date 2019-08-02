# !/usr/bin/python3
# -*- coding:utf-8 -*-
# _*_ coding:cp1254 _*_
#Ahmed Demirezen
import socket
import time
import RPi.GPIO as gpio
import Adafruit_PCA9685

#Pca 9685 setup
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

#gpio setup
gpio.setmode(gpio.BCM)

#laser setup
gpio.setup(19,gpio.OUT)
gpio.setup(26,gpio.OUT)

#clean startup
gpio.output(26,gpio.LOW)
gpio.output(19,gpio.LOW)

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
                pwm.set_pwm(3, 0, 150)
            elif data=="V 1".encode():
                pwm.set_pwm(3, 0, 195)
                print("V 1")
            elif data=="V 2".encode():
                pwm.set_pwm(3, 0, 240)
                print("V 2")
            elif data=="V 3".encode():
                pwm.set_pwm(3, 0, 285)
                print("V 3")
            elif data=="V 4".encode():
                pwm.set_pwm(3, 0, 330)
                print("V 4")
            elif data=="V 5".encode():
                pwm.set_pwm(3, 0, 375)
                print("V 5")
            elif data=="V 6".encode():
                pwm.set_pwm(3, 0, 420)
                print("V 6")
            elif data=="V 7".encode():
                pwm.set_pwm(3, 0, 465)
                print("V 7")
            elif data=="V 8".encode():
                pwm.set_pwm(3, 0, 510)
                print("V 8")
            elif data=="V 9".encode():
                pwm.set_pwm(3, 0, 555)
                print("V 9")
            elif data=="V 10".encode():
                pwm.set_pwm(3, 0, 600)
                print("V 10")
        
        #Horizontal
            elif data=="H 0".encode():
                pwm.set_pwm(0, 0, 150)
                print("H 0")
            elif data=="H 1".encode():
                pwm.set_pwm(0, 0, 195)
                print("H 1")
            elif data=="H 2".encode():
                pwm.set_pwm(0, 0, 240)
                print("H 2")
            elif data=="H 3".encode():
                pwm.set_pwm(0, 0, 285)
                print("H 3")
            elif data=="H 4".encode():
                pwm.set_pwm(0, 0, 330)
                print("H 4")
            elif data=="H 5".encode():
                pwm.set_pwm(0, 0, 375)
                print("H 5")
            elif data=="H 6".encode():
                pwm.set_pwm(0, 0, 420)
                print("H 6")
            elif data=="H 7".encode():
                pwm.set_pwm(0, 0, 465)
                print("H 7")
            elif data=="H 8".encode():
                pwm.set_pwm(0, 0, 510)
                print("H 8")
            elif data=="H 9".encode():
                pwm.set_pwm(0, 0, 555)
                print("H 9")
            elif data=="H 10".encode():
                pwm.set_pwm(0, 0, 600)
                print("H 10")        
        
        #Other        
            elif data=="close".encode():
                print("client shutting down")
                break
            
            elif data=="laser0".encode():
                gpio.output(19,gpio.LOW)
                gpio.output(19,gpio.LOW)
                print("laser0")
                
            elif data=="laser1".encode():
                gpio.output(26,gpio.LOW)
                gpio.output(19,gpio.HIGH)
                print("laser1")

        
        server.close()
        
    except ConnectionRefusedError:
        print("connection is ineffective. restarting client please wait,ErrorCode: ConnectionRefusedError")
        
    except ConnectionResetError:
        print("connection is ineffective. restarting client please wait,ErrorCode: ConnectionResetError")
