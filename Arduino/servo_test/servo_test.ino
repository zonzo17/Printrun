/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo Pan;   // create servo object to control a servo
Servo Tilt; // twelve servo objects can be created on most boards


int angle = 0;    // variable to store the servo position

void setup() 
{
  Serial.begin(9600);
  Pan.attach(9);  // attaches the servo on pin 9 to the servo object
  Tilt.attach(10);
}

void loop() 
{
  for (angle = 0; angle <= 90; angle += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree   
    Pan.write(angle);              // tell servo to go to position in variable 'pos'
    delay(15);                      // waits 15ms for the servo to reach the position
    Tilt.write(angle);
    delay(15); 
    
  }
  for (angle = 90; angle >= 0; angle -= 1) { // goes from 180 degrees to 0 degrees
    Pan.write(angle);              // tell servo to go to position in variable 'pos'
    delay(15);                        // waits 15ms for the servo to reach the position
    Tilt.write(angle);
    delay(15);
  }
}
