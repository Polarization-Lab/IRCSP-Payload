
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

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme; // I2C

unsigned long delayTime;

void setup() {
    Serial.begin(9600);
    while(!Serial);    // time to get serial running
    Serial.println(F("BME280 test"));

    unsigned status;
    
    // default settings
    status = bme.begin();  
    // You can also pass in a Wire library object like &Wire2
    // status = bme.begin(0x76, &Wire2)
    if (!status) {
        Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!");
        Serial.print("SensorID was: 0x"); Serial.println(bme.sensorID(),16);
        Serial.print("        ID of 0xFF probably means a bad address, a BMP 180 or BMP 085\n");
        Serial.print("   ID of 0x56-0x58 represents a BMP 280,\n");
        Serial.print("        ID of 0x60 represents a BME 280.\n");
        Serial.print("        ID of 0x61 represents a BME 680.\n");
        while (1) delay(10);
    }
    
    Serial.println("-- Default Test --");
    delayTime = 1000;

    Serial.println();
}


void loop() { 
    tcaselect(2)
    printValues(bme1);
    delay(delayTime);
    
    tcaselect(4)
    printValues(bme2);
    delay(delayTime);
    
    tcaselect(6)
    printValues(bme3);
    delay(delayTime);
}


void printValues(bme) {
    Serial.print("Temperature = ");
    Serial.print(bme.readTemperature());
    Serial.println(" °C");

    Serial.print("Pressure = ");

    Serial.print(bme.readPressure() / 100.0F);
    Serial.println(" hPa");

    Serial.print("Approx. Altitude = ");
    Serial.print(bme.readAltitude(SEALEVELPRESSURE_HPA));
    Serial.println(" m");

    Serial.print("Humidity = ");
    Serial.print(bme.readHumidity());
    Serial.println(" %");

    Serial.println();
}

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
    tcaselect(2);
    if(!bme1.begin())
    {
      Serial.println("No BME280 detected at Multiplexer Port 2!");
      while(1);
    }
    
    tcaselect(4);
    if(!bme2.begin())
    {
      Serial.println("No BME280 detected at Multiplexer Port 4!");
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
    Serial.print(bme1.readPressure()); Serial.print(",");
    Serial.print(bme1.readHumidity()); Serial.print(",");
    Serial.print(bme1.readTemperature()); Serial.print(",");
    Serial.print(bme2.readPressure()); Serial.print(",");
    Serial.print(bme2.readHumidity()); Serial.print(",");
    Serial.print(bme2.readTemperature()); Serial.print(",");
    Serial.print(bme3.readPressure()); Serial.print(",");
    Serial.print(bme3.readHumidity()); Serial.print(",");
    Serial.print(bme3.readTemperature()); Serial.print(",");

    //read thermister
    sensorVal = analogRead(sensorPin);
    //float thermV= sensorVal * (5.0 / 1023.0);   //converts analog read value to voltage
    Serial.print(sensorVal); Serial.print('\n');
}
