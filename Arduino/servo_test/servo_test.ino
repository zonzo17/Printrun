#include <Servo.h>

Servo Pan;   // create servo object to control a servo
Servo Tilt;

byte inByte;

void setup()
{
  Serial.begin(9600);
  Pan.attach(9);  // attaches the servo on pin 9 to the servo object
  Tilt.attach(10);
  Pan.write(45);
  Tilt.write(5);
  delay(1000);


  Serial.println("Ready");
}

void loop()
{
  // if we get a valid byte, read analog ins:
  if (Serial.available() > 0) {
    // get incoming byte:
    inByte = Serial.read();


    switch (inByte)
    {
      case '1':
        // Position 1
        Serial.println("Move to point 1");
        Pan.write(90);
        Tilt.write(160);
        break;

      case '2':
        // Position 2
        Serial.println("Move to point 2");
        Pan.write(45);
        Tilt.write(160);
        break;

      case '3':
        // Position 3
        Serial.println("Move to point 3");
        Pan.write(180);
        Tilt.write(35);
        break;

      case '4':
        // Position 4
        Serial.println("Move to point 4");
        Pan.write(90);
        Tilt.write(55);
        break;


      case '5':
        // Position 5
        Serial.println("Move to point 5");
        Pan.write(40);
        Tilt.write(70);
        break;

      case '6':
        // Position 6
        Serial.println("Move to point 6");
        Pan.write(0);
        Tilt.write(55);
        break;



      case 'r':
        Serial.println("Return to Home");
        Pan.write(45);
        Tilt.write(5);
        break;

      case '\n':
      case '\r':
        break;
        
      default:
        // statements
        Serial.println("Command unavailable");
        break;
    }
  }
}
