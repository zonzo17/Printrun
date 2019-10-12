#!/usr/bin/python

import atexit
atexit.register(lambda: input("\nPress Enter to exit."))

import time
from printrun.printcore import printcore

p = printcore('COM4', 115200)

# Wait for connection to the printer
print('Waiting for printer ...')

while not p.online:
    time.sleep(20)
print('Connected to printer !')

print('Sending home instruction (G28)')
p.send('G28')
p.send('G92 X10 Y100 Z50')

print('Disconnecting')
p.disconnect()
