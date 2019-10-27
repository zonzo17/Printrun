#!/usr/bin/python

import atexit
atexit.register(lambda: input("\nPress Enter to exit."))

print('          YOOOOO WHATS UP CRONUS !!!           ')

#import serial
import time
from printrun.printcore import printcore

printer = printcore('COM5', 115200)
#ArduinoUnoSerial = serial.Serial('COM25',9600)
#time.sleep(2)
#while 1:
 #   arduinoData = ArduinoUnoSerial.readline()


# Wait for connection to the printer
print('Waiting for printer ...')

while not printer.online:
    time.sleep(5)
print('Connected to printer !')


# Setup de l'imprimante
printer.send('G21') # Spécifie que les unités sont en mm
printer.send('G90') # Spécifie que les translations sont vers un point absolu
printer.send('G28') # Va a home

# Positions à visiter avec l'angle de caméra à adopter:
# On peut changer la structure de donné 
# ex: p_nord_est = { "position": [x,y,z], "orientation": [pan, tilt] }
# ex: p_nord_est = [x,y,z,pan,tilt]
# ex: p_nord_est = "G0 Xx Yy Zz"  <- direct ne GCODE

p_nord_est = {
        'x': 200,
        'y': 200,
        'z': 200}
        #"pan": 45, # Angle des servos moteurs
        #"tilt": 45}
p_nord_ouest = {
        'x': 20,
        'y': 200,
        'z': 200}
        #"pan": 135,
        #"tilt": 45}
p_sud_ouest = {
        'x': 20,
        'y': 20,
        'z': 70}
        #"pan": 45,
        #"tilt": 135}
p_sud_est = {
        'x': 200,
        'y': 20,
        'z': 70}
        #"pan": 135,
        #"tilt": 135}

# Liste de points à visiter durant la loupe
point_list = [ p_nord_ouest, p_nord_est, p_sud_ouest, p_sud_est ]

# Fonction pour convertir les points en instruction GCODE

def pointToGcode (point):
    return ('G0 X' + str(point['x']) + ' Y' + str(point['y']) + ' Z' + str(point['z']))


# Je fais une for loop pour faire bouger la cam à chaque point de la liste
pause_s = 30 
# J'attend une minute par point

for point in point_list:
    # Calcul du gcode à envoyer à l'imprimante
    gcode = pointToGcode(point)

    # Calcul de la trame série à envoyer au arduino, à faire dans le futur
    # orientation_message = pointToPanTiltCommand(point)

    print("\nNouveau point")
    print(point)
    print(gcode)
    # print(orientation_message)

    # On envoi les commandes aux appareils respectifs
    printer.send(gcode)
    # ArduinoUnoSerial.write(orientation_message)

    # On attend le temps prédéterminé
    time.sleep(pause_s)




print('\nDisconnecting')
printer.disconnect()
