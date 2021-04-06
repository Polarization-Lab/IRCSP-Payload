#pragma once
#ifndef BALLOONPROCESS_H
#define BALLOONPROCESS_H

#include <cstdio>
#include <fcntl.h>
#include <linux/types.h>
#include <linux/pci.h>
#include <unistd.h>
#include <string>
#include <sstream>
#include <fstream>
#include <ctime>


#define DEBUG
class Balloon
{
public:
	int fdRS232;
	int fdTelemetryOut;
	time_t LastTime;
	int LastAltitude;
	int ascentRate;
	char NMEAbuf[100];
	std::stringstream NMEA;
	static void parse(std::string NMEA, std::string GPS); //TODO define static methods
	static int getAltitude(std::string GPS);
	static time_t getTime(std::string GPS);
	Balloon();
	~Balloon();
	static int Balloon_init(void);
	void readBuf();

private:

};

int Balloon::Balloon_init(void){
	static int fd = -1;
	fd = open("/dev/ttyS1", O_RDWR );
	if (fd == -1) {
		perror("ttyS1 failed to open");
	}

	return fd;
}

void Balloon::readBuf() //needs testing
{
	char gps[1024];
	char* temp;

	NMEA.flush();
	//sets first character of NMEAbuf to \0
	do {
		do {
			sync();
			read(fdRS232, NMEAbuf, 100); //read() gets up to next \n, \r, or \0 chracter
			temp = std::strchr(NMEAbuf, '\n');
			if (temp != NULL) {
				*(temp + 1) = '\0';
			}

#ifdef DEBUG
			fprintf(stderr, NMEAbuf);
#endif // DEBUG
			NMEA << NMEAbuf;
		} while (NMEAbuf[0] == '\n'); //cleans rs232 buffer of blank entries
	} while (temp != NULL);

	//parse(NMEA.str(), gps);
	//write(fdTelemetryOut, gps, strlen(gps));
	strcpy(gps,NMEA.str().c_str());
	write(fdTelemetryOut, gps, strlen(gps));
	LastTime = getTime(gps);
	LastAltitude = getAltitude(gps);
	syncfs(fdTelemetryOut);
	
}

void Balloon::parse(std::string NMEA, std::string GPS)
{
	GPS = NMEA;
}

int Balloon::getAltitude(std::string GPS)
{
	return 0;
}

time_t Balloon::getTime(std::string GPS)
{
	return time_t();
}

Balloon::Balloon()
{
	fdRS232 = Balloon_init();
	fdTelemetryOut = open("/GPStelemetry", O_CREAT | O_WRONLY);
	if (fdTelemetryOut == -1) perror("unable to open GPStelemetry");

}

Balloon::~Balloon()
{
	close(fdRS232);
	close(fdTelemetryOut);
}

#endif // !BALLOONPROCESS_H
