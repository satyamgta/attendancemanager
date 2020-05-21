from MyQR import myqr
import os
import base64

#reading the data from 'students.txt' file
f=open('students.txt','r')
lines=f.read().split('\n')
print(lines)



#creating different qr codes for all the data
for i in range(len(lines)):
    data=lines[i].encode()
    name=base64.b64encode(data)
    version,level,qr_name = myqr.run(
    str(name),
    level='H', #four types L,M,Q,H, default is H
    version=1,  
    colorized=True,
    contrast=1.0,  #default is 1.0(float value)
    brightness=1.0,
    save_name=str(lines[i]+'.bmp'),
    save_dir=os.getcwd()  #cwd->currentworkingdirectory and default is also cwd
)

       
