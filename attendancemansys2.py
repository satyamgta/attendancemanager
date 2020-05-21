import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import pybase64
import base64
from tkinter import *

#starting camera
cam=cv2.VideoCapture(0)

#creating a text file for saving attendance
names=[]
f=open("attendance1.txt","a+")
s=time.asctime()
f.write(str(s)+'\n')

#y=50
#adding the data into file which is marked present
def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z=''.join(str(z))
        data1=decode(z)
        f.write(data1+'\n')
        return names

print('press "t" to close the frame')    
print('scanning QR...')

        
#function to mark data present 
def checkData(data):
    #global y
    data=str(data)
    if data in names:
        data1=decode(data)
        print(data1,'is already present')
    else:
        data1=decode(data)
        print('\n'+str(len(names)+1)+':'+data1,'\n'+'Present Done')
        enterData(data)
        #create(data1,y)
        #y=y+20

#decoding the data scanned by frame
def decode(data):
    c=0
    d=''
    for i in data:
        if i=="'":
            d+=i
            c=1
        if c==1 and (i!="'" or i!='"'):
            d+=i
    d1=base64.b64decode(d)
    d2=d1.decode('utf8')
    return d2

def create(data,y1):
    label1 = Label(root,text=data).place(x=30,y=y1)
##root = Tk()
##root.configure(bg='grey')
##root.title('Attendance Management System')
##root.geometry('800x800')            
            
        
#infinite loop to make the frame look like a video
while True:
    ret, frame=cam.read()  #to capture the image
    decodeObject=pyzbar.decode(frame) #to decode the qr code
    
    for Data in decodeObject:
        checkData(Data.data) #for marking the attendance
        time.sleep(1)
    #to show the image in frame
    cv2.imshow('Frame',frame)

    #closing the frame when 't' is pressed
    if cv2.waitKey(1)& 0xff==ord('t'):
        cv2.destroyAllWindows()
        #closing the camera
        cam.release()
        break

f.close()
##root.mainloop()
        
        
