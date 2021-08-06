#include <stdio.h>
#include <time.h>


class Accelerometer
{
public:
	int twifd; //points to i2c-dev file
	signed short measurementArray[3]; //records x,y,z
	bool fRead = false; //fast read mode
	int fullscale = 2; //g range
	float gValues[3];
    float total_accel;
	

	Accelerometer(); //creates new object
	Accelerometer(int twifd);
	~Accelerometer(); //destorys object
	
	
	void getAcceleration(); //gets converted acceleration into gValues
	
	
private:
	bool OAE = 0; //Freefall/motion dection configuration
	
};


