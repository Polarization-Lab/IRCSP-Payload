/***************************************************************************
reads 2 BME sensors and a thermister
thermister read found here: https://pythonforundergradengineers.com/python-arduino-potentiometer.html
BME read found here: http://cactus.io/hookups/sensors/barometric/bme280/hookup-arduino-to-multiple-bme280-barometric-pressure-sensors
 ***************************************************************************/

#include <Wire.h>


//init thermister
int sensorPin = A3;
int sensorVal;
  

void setup() {
  Serial.begin(9600);
  //Serial.println("sensorread for P3 flight"); 


  //Serial.println("BME1 Pressure (mbar),BME1 Humdity(%),BME1 Temp *C,BME2 Pressure (mbar),BME2 Humdity(%),BME2 Temp *C,V for Thermister Calc (V)");
  
}

void loop() {
    
   
    //read thermister
    sensorVal = analogRead(sensorPin);
    float thermV= sensorVal * (5.0 / 1023.0);   //converts analog read value to voltage
    Serial.print(thermV); Serial.print('\n');
    

}
