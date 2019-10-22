#!/usr/bin/python

import atexit
atexit.register(lambda: input("\nPress Enter to exit."))

print('          YOOOOO WHATS UP CRONUS !!!           ')

#import serial
import time
from printrun.printcore import printcore

p = printcore('COM5', 115200)
#ArduinoUnoSerial = serial.Serial('COM25',9600)
#time.sleep(2)
#while 1:
 #   arduinoData = ArduinoUnoSerial.readline()
    

# Wait for connection to the printer
print('Waiting for printer ...')

while not p.online:
    time.sleep(5)
print('Connected to printer !')

# Je fais une for loop pour faire bouger la cam

print('Sending X Y Z instructions (G92)')

#X = ['G0 X100','G0 Y100','G0 X100']
#Position = 0
#for i in X:
#    Position = Position + i 
#    p.send(Position)
    


print('Sending home instruction (G28)')
#p.send('G28')




print('Disconnecting')
p.disconnect()
