
/***************************************************************************
reads 3 BME sensors and a thermister
thermister read found here: https://pythonforundergradengineers.com/python-arduino-potentiometer.html
BME read found here: http://cactus.io/hookups/sensors/barometric/bme280/hookup-arduino-to-multiple-bme280-barometric-pressure-sensors
 ***************************************************************************/

#include <Wire.h>
#include <Adafruit_BME280.h>
#include <Adafruit_Sensor.h>
#include <SPI.h>
#include <SD.h>

#define TCAADDR 0x70

const int chipSelect = 4;

//Set up SD card
//File data;

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

int numberSamples = 1;

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


  Serial.print("Initializing SD card...");


  if (!SD.begin(chipSelect)) {
    Serial.println("Card Failed or Not Present!");
    while (1);
  }
  else {
    Serial.println("initialization done.");
  }


    /* Initialise sensors */
      tcaselect(1);
      if(!bme1.begin())
    {
      //Serial.println("No BME280 detected at Multiplexer Port 1!");
      //while(1);
    }
    
    tcaselect(2);
    if(!bme2.begin())
    {
      //Serial.println("No BME280 detected at Multiplexer Port 2!");
      //while(1);
    }

    tcaselect(6);
    if(!bme3.begin())
    {
      //Serial.println("No BME280 detected at Multiplexer Port 6!");
     //while(1);
   }



  File dataFile = SD.open("datalog.txt", FILE_WRITE);

  if (dataFile)
  {
    dataFile.println("Minutes Since Start,BME 1 Pressure,BME 1 Humidity,BME 1 Temperature,BME 2 Pressure,BME 2 Humidity,BME 2 Temperature,BME 3 Pressure,BME 3 Humidity,BME 3 Temperature,Context Camera Therm Val,Lens Therm Val,Housing Therm Val,Heat Sink Therm Val");
    dataFile.close();
  }
  else
  {
    Serial.println("error");
  }


  Serial.println("Minutes Since Start,BME 1 Pressure,BME 1 Humidity,BME 1 Temperature,BME 2 Pressure,BME 2 Humidity,BME 2 Temperature,BME 3 Pressure,BME 3 Humidity,BME 3 Temperature,Context Camera Therm Val,Lens Therm Val,Housing Therm Val,Heat Sink Therm Val");
}



void loop()
{
  
  //read thermister
  sensorVal = analogRead(sensorPin);
  contextVal = analogRead(contextPin);
  lensVal = analogRead(lensPin);
  heatVal = analogRead(heatPin);

  
    File dataFile = SD.open("datalog.txt", FILE_WRITE);
    if (dataFile) {

    dataFile.print(numberSamples);
    dataFile.print(",");
      
      tcaselect(1);
      dataFile.print(bme1.readPressure());
    dataFile.print(",");
    dataFile.print(bme1.readHumidity());
    dataFile.print(",");
    dataFile.print(bme1.readTemperature());
    dataFile.print(",");
    
    tcaselect(2);
    dataFile.print(bme2.readPressure());
    dataFile.print(",");
    dataFile.print(bme2.readHumidity());
    dataFile.print(",");
    dataFile.print(bme2.readTemperature());
    dataFile.print(",");
    
    tcaselect(6);
    dataFile.print(bme3.readPressure());
    dataFile.print(",");
    dataFile.print(bme3.readHumidity());
    dataFile.print(",");
    dataFile.print(bme3.readTemperature());
    dataFile.print(",");

    //float temperature1 = temperature_calculation(Therm1Val);
    dataFile.print(contextVal);
    dataFile.print(",");

    //float temperature2 = temperature_calculation(Therm2Val);
    dataFile.print(lensVal);
    dataFile.print(",");
    
    dataFile.print(sensorVal);
    dataFile.print(",");

    dataFile.print(heatVal);

    dataFile.print("\n");
    //dataFile.println(dataString);
    dataFile.close();
    Serial.println("New Line Added");
    }
    else {
    Serial.println("Error");
    }
  

  numberSamples++;
  delay(60000);
  Serial.println("delay");
  
}






    
//void loop() 
//{
  
//    //read BMEs
//    tcaselect(1);
//  // Serial.print("bme 1 ");
//    Serial.print(bme1.readPressure()); Serial.print(",");
//    Serial.print(bme1.readHumidity()); Serial.print(",");  //%
//    Serial.print(bme1.readTemperature()); Serial.print(",");   //°C
//   tcaselect(2);
//   // Serial.print("bme 2 ");
//    Serial.print(bme2.readPressure()); Serial.print(",");
//   Serial.print(bme2.readHumidity()); Serial.print(",");
//    Serial.print(bme2.readTemperature()); Serial.print(",");
//    tcaselect(6);
//   // Serial.print("bme 3 ");
//    Serial.print(bme3.readPressure()); Serial.print(",");
//    Serial.print(bme3.readHumidity()); Serial.print(",");
//    Serial.print(bme3.readTemperature()); Serial.print(",");
//
//    //read thermister
//    sensorVal = analogRead(sensorPin);
//    contextVal = analogRead(contextPin);
//    lensVal = analogRead(lensPin);
//    heatVal = analogRead(heatPin);
//    //float thermV= sensorVal * (5.0 / 1023.0);   //converts analog read value to voltage
//    Serial.print(contextVal); Serial.print(',');
//    Serial.print(lensVal); Serial.print(',');
//    Serial.print(sensorVal); Serial.print(',');
//    Serial.print(heatVal); 
//   Serial.print('\n');
//}
