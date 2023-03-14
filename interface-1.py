from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk 
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showerror,showinfo
import socket
import tkinter
import threading
import os
import sys
import socket
import time
global  server_socket,host_name,host_ip
global fichier_a ,envoyeur,receiveur,sen
global client_socket,host_ip,ars
envoyeur =True
receiveur = True
sen = True
ars = 'false'
def ecouter ():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
def sender ():
    global envoyeur,receiveur,client_socket
    
    if envoyeur:
        try:
            receiveur = False 
            client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            host_ip = ecouter()
            port = 9999

            client_socket.connect((host_ip,port))
            print("Connected Successfully")
            button_receiver.config(background="black")
            showinfo(title="Help use",message="you are actualy ready to send a file") 
        except:
            showerror(title="Help use",message="the receiver should push receive first")
    else:
        showerror(title="Help use",message="your are alredy the sender your can't be the receiver at the same")       
        
def rec():
    os.system("python server.py")           

def receive():
    global envoyeur,receiveur
    if  receiveur:
        envoyeur = False
        sen      = False
        global  server_socket,host_name,host_ip
        thread = threading.Thread(target=rec, args=())
        print('bjr')
        thread.start()
        button_send.config(background='black')
        button_sender.config(background="black")
    

def send():
    global client_socket,ars 
    if  entry1.get()=='URL_FILE' or entry1.get()=='' :
        showerror(title='Help use', message='you should upload a file first')
    else:
        if sen:
            print(entry1.get())
            file_name =entry1.get()
            real_name = file_name.split('/')
            real_name = real_name[-1]
            file_size = os.path.getsize(file_name)
            
            msg =real_name+'@'+str(file_size)+'@'+ars
            client_socket.send(msg.encode('utf-8'))
            
            with open(file_name, "rb") as file:
                c = 0
    
                start_time = time.time()

    
                while c <= file_size:
                    data = file.read(1024)
                    if not (data):
                        break
                    client_socket.sendall(data)
                    c += len(data)

    
            end_time = time.time()
            en = end_time - start_time
            showinfo(title="INFOMATION",message="the transfering of {} is ended it's took {} minute".format(real_name,en))
            sg = client_socket.recv(1024).decode('utf-8') 
            print(sg)       



window= tk.Tk()
upload= Image.open("chat_bg_ca.jpg")
image=ImageTk.PhotoImage(upload)
label= Label(window,image=image,height = 800, width =1500)
label.place(x=0,y=0)




def nouvellefenetre():
    windows=Tk()
    windows.title('file view')
    windows.geometry("600x500")
    my_scrollbar=ttk.Scrollbar(windows, orient=VERTICAL)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    a= entry1.get()
    if(a):
        fop=open(a,"r")
        my_label= Label(windows, text=fop.read()).pack()
    

def browse():
    global fichier_a
    window.filename=filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("all files","*.*"),("png files","*.png"),("jpg files","*.jpg")))
    entry1.insert(0,window.filename)
    fichier_a = window.filename
    
def deletefile():
    global fichier_a
    entry1.delete(0, END)
    fichier_a = ''
    
    
entry1= Entry(window,width=50, font=25)
entry1.place(x=200,y=170)
entry1.insert(0, "URL_FILE")


label1= Label(window, text="FILE_SHARER",font=('blue',20),width=12, height=1,bg="grey")
label1.place(x=330,y=90)

button_send=Button(window,border=0,text="SEND",width=15,bg='skyblue',fg="black", font="bold", command=send)
button_send.place(x=100,y=300)

button_sender=Button(window,border=0,text="SENDER",width=15,bg='skyblue',fg="black", font="bold", command=sender)
button_sender.place(x=100,y=380)

button_open=Button(window,text="OPEN",width=15,bg='skyblue',fg="black", font="bold", border=0, command=nouvellefenetre)
button_open.place(x=355,y=300)

button_exit=Button(window,text="CLEAN",width=15,bg='skyblue',fg="black", font="bold", border=0, command=deletefile)
button_exit.place(x=600,y=300)

button_receiver=Button(window,text="RECEIVER",width=15,bg='skyblue',fg="black", font="bold", border=0, command=receive)
button_receiver.place(x=600,y=380)

button_browse=Button(window,text="BROWSE",width=20,bg='skyblue',fg="black", font="bold", border=5, command=browse)
button_browse.place(x=330,y=450)

button_exit=Button(window,text="EXIT",width=20,bg='skyblue',fg="black", font="bold", border=5, command=window.destroy)
button_exit.place(x=330,y=500)

                                                                                          

window.title('TP_ANGLAIS')
window.geometry('850x600')
window.resizable(width=FALSE, height=FALSE)
window.mainloop() 
