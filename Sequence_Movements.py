#!/usr/bin/python

import atexit
atexit.register(lambda: input("\nPress Enter to exit."))

print('          YOOOOO WHATS UP CRONUS !!!           ')

import serial
import time
from printrun.printcore import printcore

printer = printcore('COM5', 115200)

ArduinoUnoSerial = serial.Serial('COM25',9600)
time.sleep(2)



# Wait for connection to the printer
print('Waiting for printer ...')

while not printer.online:
    time.sleep(5)
print('Connected to printer !')


# Setup de l'imprimante
printer.send('G21') # Spécifie que les unités sont en mm
printer.send('G90') # Spécifie que les translations sont vers un point absolu
ArduinoUnoSerial.write(bytes('r','utf-8'))
time.sleep(5)
print('Home')
printer.send('G28')
input("\nPress Enter to continu.")


# Positions à visiter avec l'angle de caméra à adopter:
Home = {
        'x': 0,
        'y': 0,
        'z': 0,
        "Orientation": "r" }
p1 = {
        'x': 50,
        'y': 0,
        'z': 95,
        "Orientation": "1" }# Angle des servos moteurs

p2 = {
        'x': 118,
        'y': 0,
        'z': 95,
        "Orientation": "2" }
         
p3 = {
        'x': 200,
        'y': 0,
        'z': 95,
        "Orientation": "3" }

p4 = {
        'x': 200,
        'y': 235,
        'z': 95,
        "Orientation": "4" }

p5 = {
        'x': 118,
        'y': 235,
        'z': 95,
        "Orientation": "5" }

p6 = {
        'x': 30,
        'y': 235,
        'z': 95,
        "Orientation": "6" }


# Liste de points à visiter durant la loop
point_list = [p1 , p2, p3, p4, p5, p6]
 
# Fonction pour convertir les points en instruction GCODE

def pointToGcode (point):
    return ('G0 X' + str(point['x']) + ' Y' + str(point['y']) + ' Z' + str(point['z']))


# Je fais une for loop pour faire bouger la cam à chaque point de la liste
pause_s = 10 
# J'attend une minute par point
while 1:
        for point in point_list:
                # Calcul du gcode à envoyer à l'imprimante
                gcode = pointToGcode(point)

                # Calcul de la trame série à envoyer au arduino, à faire dans le futur
                # orientation_message = pointToPanTiltCommand(point)

                print("\nNouveau point")
                print(point)
                print(gcode)

                # On envoi les commandes aux appareils respectifs
                printer.send(gcode)
                time.sleep(2)
                ArduinoUnoSerial.write(bytes(point["Orientation"],"utf-8"))
                # On attend le temps prédéterminé
                time.sleep(pause_s)



print('\nDisconnecting')
printer.disconnect()
