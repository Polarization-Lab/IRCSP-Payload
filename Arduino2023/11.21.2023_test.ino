
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
/*Adafruit_BME280 bme3;

/* Initialise thermister */
int sensorPin = A3;
int contextPin = A0; //A1
int lensPin = A2;
int heatPin = A1; //A0
int sensorVal;
int contextVal;
int lensVal;
int heatVal;

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
      tcaselect(4);
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

float temperature_calculation(float thermistorVal)
{
    float thermV = (thermistorVal * (5.0 / 1023.0));
    float res_t = (10000 * (thermV)) / (5 - (thermistorVal * (5.0 / 1023.0)));
    float a;
    float b;
    float c;
    float d;
    if (res_t <= 692600 && res_t >= 32770)
    {
      a = 0.0033570420;
      b = 0.00025214848;
      c = 0.0000033743283;
      d = -0.000000064957311;
    }
    else if (res_t < 32770 && res_t >= 3599)
    {
      a = 0.0033540170;
      b = 0.00025617244;
      c = 0.0000021400943;
      d = -0.000000072405219;
    }
    else if (res_t < 3599 && res_t >= 681.6)
    {
      a = 0.0033530481;
      b = 0.00025420230;
      c = 0.0000011431163;
      d = -0.000000069383563;
    }
    else if (res_t < 681.6&& res_t >= 187)
    {
      a = 0.0033536166;
      b = 0.000253772;
      c = 0.00000085433271;
      d = -0.000000087912262;
    }
    return (1.0 / (a + b * (log(res_t / 10000)) + (c * pow((log(res_t / 10000)),2)) + (d * pow((log(res_t / 10000)),3)))) - 273.15;
}
    
void loop() 
{
  
    //read BMEs
    tcaselect(4);
    Serial.print("bme 1 ");
    Serial.print(bme1.readPressure()); Serial.print(",");
    Serial.print(bme1.readHumidity()); Serial.print(",");  //%
    Serial.print(bme1.readTemperature()); Serial.print(",");   //°C
    tcaselect(2);
    Serial.print("bme 2 ");
    Serial.print(bme2.readPressure()); Serial.print(",");
    Serial.print(bme2.readHumidity()); Serial.print(",");
    Serial.print(bme2.readTemperature()); Serial.print(",");
    tcaselect(6);
    Serial.print("bme 3 ");
    Serial.print(bme3.readPressure()); Serial.print(",");
    Serial.print(bme3.readHumidity()); Serial.print(",");
    Serial.print(bme3.readTemperature()); Serial.print(",");

    //read thermister
    sensorVal = analogRead(sensorPin);
    contextVal = analogRead(contextPin);
    lensVal = analogRead(lensPin);
    heatVal = analogRead(heatPin);
    //float thermV= sensorVal * (5.0 / 1023.0);   //converts analog read value to voltage
    //Serial.print(contextVal); Serial.print(',');
    //Serial.print(lensVal); Serial.print(',');
    //Serial.print(sensorVal); Serial.print(',');
    Serial.print("   TESTING      ");
    float temperature1 = temperature_calculation(heatVal);
    float tempF = temperature1 * 9 / 5 + 32;
    Serial.print(tempF); Serial.print("  Fahr\t");
    Serial.print(temperature1); Serial.print("  Celc\t");
    Serial.print('\n');
}
