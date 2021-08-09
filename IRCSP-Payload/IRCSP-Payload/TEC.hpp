//
//  TEC.hpp
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/6/21.
//

#pragma once
#ifndef TECTTL_H
#define TECTTL_H
#define COEFFICIENT_MIN 0.0
#define COEFFICIENT_MAX 20.0
#define MAX_MESSAGE_SIZE 80 //characters
#define MIN_TTL_DELAY 20000 //us, takes 8.3ms to send 80 characters (160 bits) two ways @ 38400 baud


#include <fcntl.h>
#include <stdint.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <cstring>
#include <string>
#include <unistd.h>
#include <termios.h>

class TEC 
{
public:
    
    float Tr;
    bool OC;
    float PWM;

    TEC();
    TEC(float, float , float , float );
    TEC(float, float , float , float, float, float);
    TEC(float, float[3]);
    TEC(float, float[3], float, float);
    ~TEC();

    static int initTTLDIO();
    void sendParams();
    void getSingleReadout(char* outbuf);
    int clearBuffer();
    void singleByteCommand(char); //A: turn on. a: turn off. R: turn ON cyclic print. r: turn OFF cyclic print. o: print single readout
    void setParams(float, float, float, float, float, float);
    void setParams(float, float, float, float);
    void setParams(float setpoint, float PID[3], float minTemp, float maxTemp);
    void setParams(float setpoint, float PID[3]);
    int getfd();

protected:
    int fd; //filedescriptor associated ttts file descriptor for TTL
    float setpoint = 0; //degrees C
    float PID[3] = { 0, 0, 0 }; //pid coefficients
    float min = -100; //defines OC behavior and LED behavior
    float max = 100;
    struct termios tty;

    int getLineOut(char* outbuf);

private:
    void initTermios();

};

TEC::TEC() {
    fd = initTTLDIO();
    initTermios();
    singleByteCommand('a'); //dont regulate
}

TEC::TEC(float setpoint, float P, float I, float D)
{
    fd = initTTLDIO();
    initTermios();
    setParams(setpoint, P, I, D);
    //singleByteCommand('a');//dont regulate
}

TEC::TEC( float setpoint, float P, float I, float D, float minTemp, float maxTemp)
{
    fd = initTTLDIO();
    initTermios();
    setParams(setpoint, PID, minTemp, maxTemp);
    //singleByteCommand('a'); //dont regulate
}
TEC::TEC(float setpoint, float PID[3]) {
    fd = initTTLDIO();
    initTermios();
    setParams(setpoint, PID);
}

TEC::TEC(float setpoint, float PID[3], float minTemp, float maxTemp) {
    fd = initTTLDIO();
    initTermios();
    setParams(setpoint, PID, minTemp, maxTemp);
}

TEC::~TEC()
{
    close(fd);
}

void TEC::sendParams() { //might need ioctl
     int n;
     char msg[MAX_MESSAGE_SIZE];
     n = sprintf(msg, "<%.2f %.2f %.2f %.2f %.2f>\n", setpoint, PID[0], PID[1], PID[2], min, max);
     n = write(this->fd, msg, strlen(msg)); //cuts off \0 character
}

void TEC::singleByteCommand(char in) {
    char msg[2] = { in, '\n'};
    int n = write(this->fd, msg, 2);
}

int TEC::initTTLDIO() {
    int fd = open("/dev/ttyS8", O_RDWR | O_NONBLOCK );//linux header that handles chosen DIO pins
    if (fd == -1) { perror("unable to open ttyS8"); }
    else return 0;
}

inline int TEC::getfd()
{
    return fd;
}

void TEC::setParams(float setpoint, float PID[3], float minTemp, float maxTemp) {
    setParams(setpoint, PID[0], PID[1], PID[2], minTemp, maxTemp);
}

void TEC::setParams(float setpoint, float PID[3]) {
    setParams(setpoint, PID[0], PID[1], PID[2]);
}

void TEC::setParams(float setpoint, float P, float I, float D, float minTemp, float maxTemp)
{
    setParams(setpoint, P, I, D);
    min = minTemp;
    max = maxTemp;
}

void TEC::setParams(float setpoint, float P, float I, float D) {
    this->setpoint = setpoint;
    PID[0] = std::min(std::max(P, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
    PID[1] = std::min(std::max(I, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
    PID[2] = std::min(std::max(D, (float)COEFFICIENT_MIN), (float)COEFFICIENT_MAX);
    sendParams();
}

int TEC::getLineOut(char* outbuf) {
    int n = read(fd, outbuf, MAX_MESSAGE_SIZE);
    if (n > -1){
        outbuf[n] = '\0';
    }
    return n;
}

void TEC::getSingleReadout(char* outbuf) {
    int n;
    char* temp;
    clearBuffer();
    singleByteCommand('o');
    usleep(MIN_TTL_DELAY);
    do {
        n = getLineOut(outbuf);
        if (n == -1) {
            return;
        }
        temp = strstr(outbuf, "Tr=");
    } while (temp == NULL);
    Tr = strtof(temp + 3, &temp);
    OC = strtol(temp + 4, &temp, 2);
    PWM = strtof(temp + 4, &temp);
    return;
}

int TEC::clearBuffer() {
    char buf[MAX_MESSAGE_SIZE];
    int i = 0;
    while (getLineOut(buf) > -1) i++;
}

void TEC::initTermios() {
    if (tcgetattr(fd, &tty) != 0) {
        printf("Error %i from tcgetattr: %s\n", errno, strerror(errno));
    }
    cfmakeraw(&tty);
    tty.c_iflag |= IGNCR; //ignore carriage return
    tty.c_cflag &= ~(PARENB | CSTOPB); //no parity, one stop bits
    tty.c_cflag &= ~(CRTSCTS | ECHO); //disable flow control & echo; EXTREMELY IMPORTANT
    tty.c_lflag |= ICANON; //read() doesnt get up to next \n, \r, or \0 chracter
    //tty.c_iflag &= ~(IGNBRK | BRKINT | PARMRK | ISTRIP | INLCR | IGNCR | ICRNL);
    //tty.c_oflag &= ~OPOST;
    //tty.c_oflag &= ~ONLCR;
    cfsetispeed(&tty, B38400);
    if (tcsetattr(fd, TCSANOW, &tty) != 0) {
        printf("Error %i from tcsetattr: %s\n", errno, strerror(errno));
    }
}

#endif // !TECTTL_H
