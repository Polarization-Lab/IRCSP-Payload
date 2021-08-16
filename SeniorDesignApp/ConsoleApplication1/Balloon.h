#pragma once
#ifndef BALLOON_H
#define BALLOON_H

#include <cstdio>
#include <fcntl.h>
#include <linux/types.h>
#include <linux/pci.h>
#include <unistd.h>
#include <string>
#include <sstream>
#include <fstream>
#include <ctime>
#include <time.h>
#include <termios.h>

#define MAX_NMEA_SIZE 82

class Balloon
{
public:
	int fdRS232;
	int fdTelemetryOut;
	struct tm lastTime;
	float lastAltitude = __FLT_MAX__; //FORCES FIRST ASCENT RATE TO BE NEGATIVE
	double ascentRate = 0; //M per minute
	char NMEAbuf[MAX_NMEA_SIZE];
	static void parse(char*, tm*, float*); //TODO define static methods
	Balloon();
	~Balloon();
	static int Balloon_init(void);
	static float subtracttm(tm source, tm subtractor);
	void readBuf();
	struct termios tty;
private:

};

int Balloon::Balloon_init(void){
	static int fd = -1;
	fd = open("/dev/ttyS1", O_RDWR | O_NONBLOCK | O_NOCTTY);
	if (fd == -1) {
		perror("ttyS1 failed to open");
	}
	return fd;
}

void Balloon::readBuf() //needs testing
{
	int n = -1;
	tm pTime;
	float pAltitude;
	do {
		//NMEAbuf[0] = '\0';
		n = read(fdRS232, NMEAbuf, MAX_NMEA_SIZE);
		if (n == -1) {
			break;
		}
		write(fdTelemetryOut, NMEAbuf, n);
		NMEAbuf[n] = '\0';
		pTime = lastTime;
		pAltitude = lastAltitude;
		parse(NMEAbuf, &lastTime, &lastAltitude);
		ascentRate = (lastAltitude - pAltitude) / subtracttm(lastTime, pTime); //m/s
#ifdef DEBUG
		fprintf(stderr, NMEAbuf);
#endif // DEBUG
	} while (n > -1);
	syncfs(fdTelemetryOut); //extraneous function due to O_Sync
}

void Balloon::parse(char* NMEAmsg, tm* time, float* altitude)
{
	char GPGGA[] = "$GPGGA";
	char temp[3];
	char* pos;
	for (int i = 0; i <= 5; i++) {
		if (GPGGA[i] != NMEAmsg[i]) return;
	}
	pos = strchr(NMEAmsg, ',') + 1;
	if (time != NULL) {
		temp[0] = pos[0];
		temp[1] = pos[1];
		temp[2] = '\0';
		time->tm_hour = atoi(temp);
		temp[0] = pos[2];
		temp[1] = pos[3];
		time->tm_min = atoi(temp); 
		time->tm_sec = atoi(pos + 4); //last one doesnt need temp constructor
	}
	if (altitude != NULL) {
		for (int i = 0; i < 8; i++) {
			pos = strchr(pos, ',') + 1;
		}
		*altitude = strtof(pos, NULL);
		pos = strchr(pos, ',') + 1;
		if (pos[0] != 'M') *altitude *= 0.3048; //ft to M
	}
}

float Balloon::subtracttm(tm source, tm subtractor) {
	float timedif;
	if (source.tm_sec < subtractor.tm_sec) {
		source.tm_sec += 60;
		source.tm_min -= 1;
	}
	timedif = (source.tm_sec - subtractor.tm_sec);

	if (source.tm_min < subtractor.tm_min) {
		source.tm_min += 60;
		source.tm_hour -= 1;
	}
	
	timedif += 60 * (source.tm_min - subtractor.tm_min);

	if (source.tm_hour < subtractor.tm_hour) source.tm_hour += 24;
	timedif += 3600 * (source.tm_hour - subtractor.tm_hour);

	return timedif;
}

Balloon::Balloon()
{
	fdRS232 = Balloon_init();
	fdTelemetryOut = open("/GPStelemetry", O_CREAT | O_WRONLY | O_SYNC); //append to end, consider dir searching 
	if (fdTelemetryOut == -1) perror("unable to open GPStelemetry");
	if (tcgetattr(fdRS232, &tty) != 0) {
		printf("Error %i from tcgetattr: %s\n", errno, strerror(errno));
	}
	cfmakeraw(&tty);
	tty.c_cflag &= ~(PARENB | CSTOPB); //no parity, single stop bit
	tty.c_cflag &= ~(CRTSCTS | ECHO); //no flow control no echo
	tty.c_lflag |= ICANON; //canon read() gets up to next \n, \r, or \0 chracter
	cfsetispeed(&tty, B600); //baud 600

	if (tcsetattr(fdRS232, TCSANOW, &tty) != 0) {
		printf("Error %i from tcsetattr: %s\n", errno, strerror(errno));
	}

}

Balloon::~Balloon()
{
	close(fdRS232);
	close(fdTelemetryOut);
}

#endif // !BALLOONPROCESS_H
