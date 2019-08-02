# !/usr/bin/python3
# -*- coding:utf-8 -*-
# _*_ coding:cp1254 _*_
#Ahmed Demirezen

#importing library
import socket
import tkinter as tk

#this step was assing server variable
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

class login_panel:
    def __init__(self,screen):
        self.control_unit=0
        self.control_unit_4panel=0

        frame=tk.Frame(screen)
        frame.pack()
             
        self.l1=tk.Label(frame,text="User Id:")
        self.l1.grid(row=0,column=0)
        
        self.e1=tk.Entry(frame)
        self.e1.grid(row=0,column=1)

        self.l2=tk.Label(frame,text="Pass:")
        self.l2.grid(row=1,column=0)

        self.e2=tk.Entry(frame)
        self.e2.grid(row=1,column=1)

        self.b1=tk.Button(frame,text="Ok",command=self.control,padx=10,pady=2)
        self.b1.grid(row=3,column=0)

        self.l3=tk.Label(frame)
        self.l3.grid(row=4,column=0)
    def control(self):#username and password are checked
        if (self.e1.get()=="admin" and self.e2.get()=="123"):
            print("\nlogin succes")
            self.control_unit=1
            window.destroy()
        else:
            self.l3["text"]="username or password is wrong !!!"
            print("\nusername or password is wrong !!!")

class connection:#ip and port settings 
    def __init__(self,screen_1):
        self.control_unit_1=0
        
        frame=tk.Frame(screen_1)
        frame.pack()

        self.l3=tk.Label(frame,text="Ip|Port:")
        self.l3.grid(row=0,column=0)

        self.l1=tk.Label(frame,text="Host Ip:")
        self.l1.grid(row=1,column=0)

        self.e1=tk.Entry(frame)
        self.e1.grid(row=1,column=1)

        self.l2=tk.Label(frame,text="Port:")
        self.l2.grid(row=2,column=0)

        self.e2=tk.Entry(frame)
        self.e2.grid(row=2,column=1)

        self.b1=tk.Button(frame,text="Ok",padx=10,pady=2,command=self.server_c)
        self.b1.grid(row=3,column=0)

        self.b2=tk.Button(frame,text="Test",padx=10,pady=2,command=self.ip_port)
        self.b2.grid(row=3,column=1)

    def ip_port(self):
        self.l3["text"]="Ip|Port:",self.e1.get(),"|",self.e2.get()

    def server_c(self):
        try:
            self.host=self.e1.get()
            self.port=int(self.e2.get())

            server.bind((self.host,self.port))

            window_2.destroy()
        except ValueError:
            self.l3["text"]="ValueError Please Enter the Number"
        

class control_panel:#main window
    def __init__(self,screen_2):

        self.laser_bool=False

        frame_1=tk.Frame(screen_2)
        frame_1.place(x=0,y=0)

        frame_2=tk.Frame(screen_2)
        frame_2.place(x=0,y=150)
        
        frame_2.focus_set()
        frame_2.bind("<Key>",self.c_w_kb)#for the keyboard control

        self.s1=tk.Scale(frame_1,from_=10,to =0, orient="vertical",command=self.scale_v)#vertical control scale
        self.s1.grid(row=0,column=0)

        self.s1.set(5)

        self.s2=tk.Scale(frame_1,from_=10,to =0, orient="horizontal",command=self.scale_h)#horizontal control scale
        self.s2.grid(row=0,column=1)

        self.s2.set(5)

        self.l1=tk.Label(frame_2,text="Control with W A S D")
        self.l1.grid(row=0,column=0)

        self.s3=tk.Scale(frame_2,from_=0,to=1,orient="horizontal",command=self.laser)#laser control scale
        self.s3.grid(row=1,column=0)

        self.l2=tk.Label(frame_2,text="Laser")
        self.l2.grid(row=1,column=1)

        self.b2=tk.Button(frame_1,text=("Close the Client"),command=self.c_t_c)#close button
        self.b2.grid(row=0,column=3)

        self.scale_l=0
        
    def scale_v(self,angle):
        print("V ",self.s1.get())
        message="V "+str(self.s1.get())
        addr.send(message.encode())

    def scale_h(self,angle):
        print("H ",self.s2.get())
        message="H "+str(self.s2.get())
        addr.send(message.encode())

    def c_t_c(self):#close the client
        addr.send("close".encode())
        
    def laser(self,angle):    
        self.laser_m="laser"+str(self.s3.get())
        addr.send(self.laser_m.encode())
    
    def c_w_kb(self,event):#control with keyboard
        self.scale_l=self.s1.get()
        self.scale_2=self.s2.get()
        
        
            
        if event.char=="s" or event.char=="S":
            if int(self.scale_l)==0:
                pass
            else:
                self.scale_l=self.scale_l-1
                self.s1.set(int(self.scale_l))
                message="V "+str(self.s1.get())
                addr.send(message.encode())
                print("V ",self.s1.get())
                

        elif event.char=="w" or event.char=="W":
            if int(self.scale_l)==10:
                pass
            else:
                self.scale_l=self.scale_l+1
                self.s1.set(int(self.scale_l))
                message="V "+str(self.s1.get())
                addr.send(message.encode())
                print("V ",self.s1.get())
                

        elif event.char=="d" or event.char=="D":                                                                                                       
            if int(self.scale_2)==0:
                pass
            else:
                self.scale_2=self.scale_2-1
                self.s2.set(int(self.scale_2))
                message="H "+str(self.s2.get())
                addr.send(message.encode())
                print("H ",self.s2.get())
                

        elif event.char=="a" or event.char=="A":
            if int(self.scale_2)==10:
                pass
            else:
                self.scale_2=self.scale_2+1
                self.s2.set(int(self.scale_2))
                message="H "+str(self.s2.get())
                addr.send(message.encode())
                print("H ",self.s2.get())

        elif event.char=="l" or event.char=="L":
            
            if self.laser_bool==False:
                self.laser_bool=True
                self.s3.set(1)
                addr.send("laser1".encode())
            elif self.laser_bool==True:
                self.laser_bool=False
                self.s3.set(0)
                addr.send("laser0".encode())
                
                  
###Windows    
window=tk.Tk()
window.geometry("300x100")
window.title("Login Panel")
login_screen=login_panel(window)
window.mainloop()
#
window_2=tk.Tk()
window_2.geometry("300x100")
window_2.title("Connection")
if (login_screen.control_unit == 1):
    
    login_screen_2=connection(window_2)
    login_screen_2.control_unit_1=1
    login_screen.control_unit_4panel=1
else:
    window_2.destroy()
window_2.mainloop()
##Server 
server.listen(1)
print("connection is waiting")
addr,ip = server.accept()
print("connection is succes\nConnecnted ip:",ip,addr)
addr.send("command".encode())
##
#
window_3=tk.Tk()
window_3.title("Control Panel")
window_3.geometry("300x300")
try:    
    if (login_screen_2.control_unit_1==1):
        login_screen_3=control_panel(window_3)
    else:
        window_3.destroy()
except NameError:
    if (login_screen.control_unit_4panel==1):
        login_screen_3=control_panel(window_3)
    else:
        window_3.destroy()
window_3.mainloop()
#
###




















































