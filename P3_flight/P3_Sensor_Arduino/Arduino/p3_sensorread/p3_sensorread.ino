/***************************************************************************
reads 2 BME sensors and a thermister
thermister read found here: https://pythonforundergradengineers.com/python-arduino-potentiometer.html
BME read found here: http://cactus.io/hookups/sensors/barometric/bme280/hookup-arduino-to-multiple-bme280-barometric-pressure-sensors
 ***************************************************************************/

#include <Wire.h>
#include "cactus_io_BME280_I2C.h"

// Create two BME280 instances
BME280_I2C bme1(0x77);  // I2C using default 0x77 
BME280_I2C bme2(0x76);  // I2C using address 0x76

//init thermister
int sensorPin = A3;
int sensorVal;
  

void setup() {
  Serial.begin(9600);
  //Serial.println("sensorread for P3 flight"); 

  if (!bme1.begin()) {
    Serial.println("Could not find a First BME280 sensor, check wiring!");
    while (1);
  }
  
  if (!bme2.begin()) {
    Serial.println("Could not find a Second BME280 sensor, check wiring!");
    while (1);
  }

  //Serial.println("BME1 Pressure (mbar),BME1 Humdity(%),BME1 Temp *C,BME2 Pressure (mbar),BME2 Humdity(%),BME2 Temp *C,V for Thermister Calc (V)");
  
}

void loop() {

    delay(1000);
    
    //read BME
    bme1.readSensor();
    bme2.readSensor();

    Serial.print(bme1.getPressure_MB()); Serial.print(",");
    Serial.print(bme1.getHumidity()); Serial.print(",");
    Serial.print(bme1.getTemperature_C()); Serial.print(",");
    Serial.print(bme2.getPressure_MB()); Serial.print(",");
    Serial.print(bme2.getHumidity()); Serial.print(",");
    Serial.print(bme2.getTemperature_C()); Serial.print(",");

    //read thermister
    sensorVal = analogRead(sensorPin);
    //float thermV= sensorVal * (5.0 / 1023.0);   //converts analog read value to voltage
    Serial.print(sensorVal); Serial.println();
    

}
