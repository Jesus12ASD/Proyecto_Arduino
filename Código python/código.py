import mouse, sys
import time 
import serial as s

mouse.FAILSAFE=False
ArduinoSerial = s.Serial('com3',9600)
time.sleep(1)                             

while 1:
   data=str(ArduinoSerial.readline().decode('ascii'))
   (x,y,z)=data.split(":")          
   (X,Y)=mouse.get_position()        
   (x,y)=(int(x),int(y))                           
   mouse.move(X+x,Y-y)      
   if '1' in z:                        
      mouse.click(button="left")
     
