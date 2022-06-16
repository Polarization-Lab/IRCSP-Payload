/***************************************************************************
  This is a library for the BME280 humidity, temperature & pressure sensor
  
  These sensors supports I2C or SPI to communicate, 2 or 4 pins are required
  to interface. However this sketch is using I2C for communications and only 
  needs 2 wires for communication
 ***************************************************************************/

#include <Wire.h>
#include "cactus_io_BME280_I2C.h"

// Create two BME280 instances
BME280_I2C bme1(0x77);  // I2C using default 0x77 
BME280_I2C bme2(0x76);  // I2C using address 0x76

void setup() {
  Serial.begin(9600);
  Serial.println("Multi Bosch BME280 Barometric Pressure - Humidity - Temp Sensor | cactus.io"); 

  if (!bme1.begin()) {
    Serial.println("Could not find a First BME280 sensor, check wiring!");
    while (1);
  }
  
  if (!bme2.begin()) {
    Serial.println("Could not find a Second BME280 sensor, check wiring!");
    while (1);
  }
  
  Serial.println("Device\tPressure\tHumdity\t\tTemp *C");
  
}

void loop() {

    Serial.print("BME 1\t");
    bme1.readSensor();
    Serial.print(bme1.getPressure_MB()); Serial.print("\t\t");    // Pressure in millibars
    Serial.print(bme1.getHumidity()); Serial.print("\t\t");
    Serial.print(bme1.getTemperature_C()); Serial.println(" *C\t");
    
    delay(1000);

    Serial.print("BME 2\t");
    bme2.readSensor();
    Serial.print(bme2.getPressure_MB()); Serial.print("\t\t");   
    Serial.print(bme2.getHumidity()); Serial.print("\t\t");
    Serial.print(bme2.getTemperature_C()); Serial.println(" *C\t");

    // add a 1 second delay to slow down the output
    delay(1000);
}
