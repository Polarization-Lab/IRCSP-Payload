#pragma once
#ifndef TECTTL_H
#define TECTTL_H
#define TIMEOUT 20
#define COEFFICIENT_MIN 0.0
#define COEFFICIENT_MAX 20.0
#define MAX_MESSAGE_SIZE 64
#define DEBUG

#include <fcntl.h>
#include <stdint.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <cstring>
#include <string>
#include <unistd.h>
#include <termios.h>

class TECTTL //TODO:: Use SYSCON to optimize listening time
{
	int fd; //filedescriptor associated ttts file descriptor for TTL
	float setpoint; //degrees C
	float PID[3] = { 0, 0, 0 }; //pid coefficients 
	float min = -70; //defines OC behavior and LED behavior 
	float max = 70;
	struct termios tty;

public:
	TECTTL();
	TECTTL(float, float , float , float );
	TECTTL(float, float , float , float, float, float);
	TECTTL(float, float[3]);
	TECTTL(float, float[3], float, float);
	~TECTTL();

	static int initTTLDIO();
	void sendParams();
	void getPrintOut(char* outbuf); //move this to private later
	void clearBuffer();
	void singleByteCommand(char); //A: turn on. a: turn off. R: turn ON cyclic print. r: turn OFF cyclic print. o: print single readout
	void setParams(float, float, float, float, float, float);
	void setParams(float, float, float, float);
	void setParams(float setpoint, float PID[3], float minTemp, float maxTemp);
	void setParams(float setpoint, float PID[3]);
	
private:
	void initTermios();
};

TECTTL::TECTTL() {
	fd = initTTLDIO();
	initTermios();
	singleByteCommand('a'); //dont regulate 
}

TECTTL::TECTTL(float setpoint, float P, float I, float D)
{
	fd = initTTLDIO();
	initTermios();
	setParams(setpoint, P, I, D);
	//singleByteCommand('a');//dont regulate
}

TECTTL::TECTTL( float setpoint, float P, float I, float D, float minTemp, float maxTemp)
{
	fd = initTTLDIO();
	initTermios();
	setParams(setpoint, PID, minTemp, maxTemp);
	//singleByteCommand('a'); //dont regulate
}
TECTTL::TECTTL(float setpoint, float PID[3]) {
	fd = initTTLDIO();
	initTermios();
	setParams(setpoint, PID);
}

TECTTL::TECTTL(float setpoint, float PID[3], float minTemp, float maxTemp) {
	fd = initTTLDIO();
	initTermios();
	setParams(setpoint, PID, minTemp, maxTemp);
}

TECTTL::~TECTTL()
{
	close(fd);
}

void TECTTL::sendParams() { //might need ioctl
	 int n;
	 std::string msg;
	 msg = '<' + std::to_string(this->setpoint) + ' ' + std::to_string(this->PID[0]) + ' ' + std::to_string(this->PID[1]) + ' ' + std::to_string(this->PID[2]) + ' ' + std::to_string(this->min) + ' ' + std::to_string(this->max) + '>' + '\r' + '\n';
	 char message[msg.length()];
	 strcpy(message, msg.c_str());
	 n = write(this->fd, message, strlen(message)); //cuts off \0 character
}

void TECTTL::singleByteCommand(char in) {
	char msg[3] = { in, '\r', '\n'};
	int n = write(this->fd, msg, 3);
}

int TECTTL::initTTLDIO() {
	int fd = open("/dev/ttyS8", O_RDWR | O_NONBLOCK | O_NOCTTY);//linux header that handles chosen DIO pins
	if (fd == -1) { perror("unable to open ttyS6"); }
	else return fd;
}

void TECTTL::setParams(float setpoint, float PID[3], float minTemp, float maxTemp) {
	setParams(setpoint, PID[0], PID[1], PID[2], minTemp, maxTemp);
}

void TECTTL::setParams(float setpoint, float PID[3]) {
	setParams(setpoint, PID[0], PID[1], PID[2]);
}

void TECTTL::setParams(float setpoint, float P, float I, float D, float minTemp, float maxTemp)
{
	setParams(setpoint, P, I, D);
	min = minTemp;
	max = maxTemp;
}

void TECTTL::setParams(float setpoint, float P, float I, float D) {
	this->setpoint = setpoint;
	PID[0] = std::min(std::max(P, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	PID[1] = std::min(std::max(I, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	PID[2] = std::min(std::max(D, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
	sendParams();
}

void TECTTL::getPrintOut(char* outbuf) {
	int n = read(fd, outbuf, MAX_MESSAGE_SIZE);
	if (n > -1){
		outbuf[n] = '\0';
#ifdef DEBUG
		fprintf(stderr, outbuf);
#endif // DEBUG
	} 
}


void TECTTL::initTermios() {
	if (tcgetattr(fd, &tty) != 0) {
		printf("Error %i from tcgetattr: %s\n", errno, strerror(errno));
	}
	cfmakeraw(&tty);
	tty.c_cflag &= ~(PARENB | CSTOPB);
	tty.c_lflag &= ~ICANON; //read() doesnt get up to next \n, \r, or \0 chracter
	//tty.c_iflag &= ~(IGNBRK | BRKINT | PARMRK | ISTRIP | INLCR | IGNCR | ICRNL);
	//tty.c_oflag &= ~OPOST;
	//tty.c_oflag &= ~ONLCR;
	if (tcsetattr(fd, TCSANOW, &tty) != 0) {
		printf("Error %i from tcsetattr: %s\n", errno, strerror(errno));
	}
}

#endif // !TECTTL_H
