#pragma once
#ifndef UARTSERIAL_H
#define UARTSERIAL_H

#include <fcntl.h>
#include <string.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <stdint.h>

int initTTLDIO() {
	int fd = open("/dev/ttts6", O_RDWR);//linux header that handles chosen DIO pins
	if (fd = -1) perror("unable to open ttts6");
	else return fd;
}


#endif