#!/usr/bin/python

import atexit
import re
import time

atexit.register(lambda: input("\nPress Enter to exit."))

print('          YOOOOO WHATS UP CRONUS !!!           ')

#import serial
from printrun.printcore import printcore

p = printcore('COM5', 115200)

# Wait for connection to the printer
print('Waiting for printer ...')

while not p.online:
    time.sleep(2)
print('Connected to printer !')

# Retourne à sa position de départ et ensuite bouge 
Add_Pos = ['X20','Y20','Z20']
Init_Pos =  ['X0','Y0','Z0']
p.send('G28')
for i in Init_Pos:
    Init_Pos = Init_Pos + i 
    p.send('G0 Init_Pos')

print('Disconnecting')
p.disconnect()