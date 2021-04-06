#pragma once
#ifndef TECTTL_H
#define TECTTL_H
#define COEFFICIENT_MIN 0.0
#define COEFFICIENT_MAX 20.0
#define DEBUG

#include <fcntl.h>
#include <stdint.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <cstring>
#include <string>
#include <unistd.h>

class TECTTL
{
	int fd; //filedescriptor associated ttts file descriptor for TTL
	float setpoint; //degrees C
	float PID[3] = { 0, 0, 0 }; //pid coefficients 
	float min = -70; //defines OC behavior and LED behavior 
	float max = 70;

public:
	TECTTL();
	TECTTL(float, float , float , float );
	TECTTL(float, float , float , float, float, float);
	TECTTL(float, float[3]);
	TECTTL(float, float[3], float, float);
	~TECTTL();

	static int initTTLDIO();
	void sendParams();
	void getPrintOut(char*);
	void clearBuffer();
	void singleByteCommand(char); //A: turn on. a: turn off. R: turn ON cyclic print. r: turn OFF cyclic print. o: print single readout
	void setParams(float, float, float, float, float, float);
	void setParams(float, float, float, float);
	
private:

};

TECTTL::TECTTL() {
	fd = initTTLDIO();
	singleByteCommand('a'); //dont regulate 
}

TECTTL::TECTTL(float setpoint, float P, float I, float D)
{
	fd = initTTLDIO();
	this->setpoint = setpoint;
	//define setpoint 
	PID[0] = std::min(std::max(P,(float) COEFFICIENT_MIN),(float) COEFFICIENT_MAX);
	PID[1] = std::min(std::max(I, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	PID[2] = std::min(std::max(D, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	//singleByteCommand('a');//dont regulate
	sendParams();
}

TECTTL::TECTTL( float setpoint, float P, float I, float D, float minTemp, float maxTemp)
{
	fd = initTTLDIO();
	this->setpoint = setpoint;	//define setpoint 
	PID[0] = std::min(std::max(P, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	PID[1] = std::min(std::max(I, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	PID[2] = std::min(std::max(D, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	min = minTemp;
	max = maxTemp;
	//singleByteCommand('a'); //dont regulate
	sendParams();
}
TECTTL::TECTTL(float setpoint, float PID[3]) {
	this->setpoint = setpoint;
	this->PID[0] = std::min(std::max(PID[0], (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	this->PID[1] = std::min(std::max(PID[1], (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	this->PID[2] = std::min(std::max(PID[2], (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	sendParams();
}

TECTTL::TECTTL(float setpoint, float PID[3], float minTemp, float maxTemp) {
	this->setpoint = setpoint;
	this->PID[0] = std::min(std::max(PID[0], (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	this->PID[1] = std::min(std::max(PID[1], (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	this->PID[2] = std::min(std::max(PID[2], (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	min = minTemp;
	max = maxTemp;
	sendParams();
}

TECTTL::~TECTTL()
{
	close(fd);
}

void TECTTL::sendParams() { //might need ioctl
	 std::string msg;
	 msg = '<' + std::to_string(this->setpoint) + ' ' + std::to_string(this->PID[0]) + ' ' + std::to_string(this->PID[1]) + ' ' + std::to_string(this->PID[2]) + ' ' + std::to_string(this->min) + ' ' + std::to_string(this->max) + '>' + '\r' + '\n';
	 char message[msg.length()];
	 strcpy(message, msg.c_str());
	 write(this->fd, message, strlen(message));
}

void TECTTL::singleByteCommand(char in) {
	char msg[3] = { in, '\n', '\r' };
	write(this->fd, msg, 3);
}

int TECTTL::initTTLDIO() {
	int fd = open("/dev/ttyS8", O_RDWR | O_SYNC);//linux header that handles chosen DIO pins
	if (fd == -1) { perror("unable to open ttyS6"); }
	else return fd;
}

void TECTTL::setParams(float setpoint, float P, float I, float D, float minTemp, float maxTemp)
{
	this->setpoint = setpoint;
	PID[0] = std::min(std::max(P, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	PID[1] = std::min(std::max(I, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	PID[2] = std::min(std::max(D, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	min = minTemp;
	max = maxTemp;
	sendParams();
}

void TECTTL::setParams(float setpoint, float P, float I, float D) {
	this->setpoint = setpoint;
	PID[0] = std::min(std::max(P, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	PID[1] = std::min(std::max(I, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	PID[2] = std::min(std::max(D, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	sendParams();
}

void TECTTL::getPrintOut(char* buf) {
	do { 
		syncfs(fd);
		//buf[0] = '\0';
		read(fd, buf, 256); 
		*(std::strchr(buf, '\n') + 1) = '\0';
#ifdef DEBUG
		fprintf(stderr, buf);
#endif // DEBUG
	} 
	while (buf[0] == '\n');
}

void TECTTL::clearBuffer() {
	char temp[256] = "EOF";
	write(fd, temp, strlen(temp));
	do {
		syncfs(fd);
		read(fd, temp, 256);
#ifdef DEBUG
		fprintf(stderr, temp);
#endif // DEBUG

	} while (strcmp(temp,"EOF") != 0); //read adds a \n?
}


#endif // !TECTTL_H
