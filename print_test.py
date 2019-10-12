#!/usr/bin/python

import atexit
atexit.register(lambda: input("\nPress Enter to exit."))

import time
from printrun.printcore import printcore

p = printcore('/dev/ttyACM0', 115200)

# Wait for connection to the printer
print('Waiting for printer ...')

while not p.online:
    time.sleep(20)
print('Connected to printer !')

print('Sending home instruction (G28)')
p.send('G28')

print('Disconnecting')
p.disconnect()
