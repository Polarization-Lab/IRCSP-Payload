#include "TECTTL.h"
#include <string>
#include <cstdlib>
using namespace std;

// //creates TTL string to send to controller, sends adress to first character
void TECTTL::sendParams() {
	string message = "< " + to_string(this->setpoint) + ' ' + to_string(this->proportional) + ' ' + to_string(this->differential) + ' ' + to_string(this->min) + ' ' + to_string(this->max) + '\r' + '\n';
	write(this->fd, &message[0], sizeof(message));
}

static int initTTLDIO() {
	int fd = open("/dev/ttts6", O_RDWR);//linux header that handles chosen DIO pins
	if (fd = -1) perror("unable to open ttts6");
	else return fd;
}