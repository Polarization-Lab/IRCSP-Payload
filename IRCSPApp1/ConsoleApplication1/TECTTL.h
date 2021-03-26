#pragma once
#ifndef TECTTL_H
#define TECTTL_H
#define COEFFICIENT_MIN 0.0
#define COEFFICIENT_MAX 20.0

#include "UARTserial.h"
#include <stdint.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>

class TECTTL
{
	int fd; //filedescriptor associated ttts file descriptor for TTL
	float setpoint; //degrees C
	float proportional;
	float integral;
	float differential;
	float min; //defines OC behavior and LED behavior 
	float max;

public:
	TECTTL(int, float, float , float , float );
	TECTTL(int, float, float , float , float, float, float);

	void sendParams();
	void getPrintOut(char*);
	void singleByteCommand(char);
	void setParams(float, float, float, float, float, float);
	void setParams(float, float, float, float);
private:

};

TECTTL::TECTTL(int filedescriptor, float setpoint, float P, float I, float D)
{
	fd = filedescriptor;
	this->setpoint = setpoint;
	//define setpoint 
	proportional = std::min(std::max(P,(float) COEFFICIENT_MIN),(float) COEFFICIENT_MAX);
	integral = std::min(std::max(I, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	differential = std::min(std::max(D, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	min = -70; 
	max = 70;
	this->sendParams();
}

TECTTL::TECTTL(int filedescriptor, float setpoint, float P, float I, float D, float minTemp, float maxTemp)
{
	fd = filedescriptor;
	this->setpoint = setpoint;
	//define setpoint 
	proportional = std::min(std::max(P, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	integral = std::min(std::max(I, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	differential = std::min(std::max(D, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	min = minTemp;
	max = maxTemp;
	this->sendParams();
}




#endif // !TECTTL_H
