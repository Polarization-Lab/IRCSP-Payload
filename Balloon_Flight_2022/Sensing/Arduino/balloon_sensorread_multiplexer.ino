
/***************************************************************************
reads 3 BME sensors and a thermister
thermister read found here: https://pythonforundergradengineers.com/python-arduino-potentiometer.html
BME read found here: http://cactus.io/hookups/sensors/barometric/bme280/hookup-arduino-to-multiple-bme280-barometric-pressure-sensors
 ***************************************************************************/

#include <Wire.h>
#include <Adafruit_BME280.h>
#include <Adafruit_Sensor.h>

#define TCAADDR 0x70

/* Initialize BMEs */
Adafruit_BME280 bme1;
Adafruit_BME280 bme2;
Adafruit_BME280 bme3;

/* Initialise thermister */
int sensorPin = A3;
int sensorVal;

/* for reading altitude
#define SEALEVELPRESSURE_HPA (1013.25)
Serial.print(bme.readAltitude(SEALEVELPRESSURE_HPA));
*/

unsigned long delayTime;

void tcaselect(uint8_t i) {
  if (i > 7) return;
 
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();  
}

void setup()
{
    while (!Serial);
    delay(1000);

    Wire.begin();
    
    Serial.begin(9600);

    /* Initialise sensors */
    tcaselect(1);
    if(!bme1.begin())
    {
      Serial.println("No BME280 detected at Multiplexer Port 1!");
      while(1);
    }
    
    tcaselect(2);
    if(!bme2.begin())
    {
      Serial.println("No BME280 detected at Multiplexer Port 2!");
      while(1);
    }

    tcaselect(6);
    if(!bme3.begin())
    {
      Serial.println("No BME280 detected at Multiplexer Port 6!");
      while(1);
    }

}

    
void loop() 
{
  
    //read BMEs
    tcaselect(2);
    Serial.print(bme1.readPressure()); Serial.print(",");
    Serial.print(bme1.readHumidity()); Serial.print(",");  //%
    Serial.print(bme1.readTemperature()); Serial.print(",");   //°C
    tcaselect(4);
    Serial.print(bme2.readPressure()); Serial.print(",");
    Serial.print(bme2.readHumidity()); Serial.print(",");
    Serial.print(bme2.readTemperature()); Serial.print(",");
    tcaselect(6);
    Serial.print(bme3.readPressure()); Serial.print(",");
    Serial.print(bme3.readHumidity()); Serial.print(",");
    Serial.print(bme3.readTemperature()); Serial.print(",");

    //read thermister
    sensorVal = analogRead(sensorPin);
    //float thermV= sensorVal * (5.0 / 1023.0);   //converts analog read value to voltage
    Serial.print(sensorVal); Serial.print('\n');
}
