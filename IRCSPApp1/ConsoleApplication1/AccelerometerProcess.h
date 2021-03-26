#ifndef ACCELEROMETERPROCESS_H
#define	ACCELEROMETERPROCESS_H
#include "i2c-dev.h"
#include <linux/pci.h>
#include <fcntl.h>
#include <stdint.h>
#include <linux/types.h>
#include <sys/ioctl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <cstddef>
#include <cstdio>
#define ACCELEROMETER_CHIP_ADDRESS 0x1c

static int accelerometer_init(void);
static int accelerometer_read(int twifd, uint8_t* data, uint16_t addr, short int bytes);
static int accelerometer_write(int twifd, uint8_t* data, uint16_t addr, short int bytes);
//defined fuct
static void accelerometer_reset(int twifd) {
	unsigned char command;
	accelerometer_write(twifd, &(command = 0b01000000), 0x2B, 1); //set reset int cntl reg 2
	usleep(100000);
	accelerometer_write(twifd, &(command = 0b1), 0x2A, 1); //set active in ctrl reg 
}

static void accelerometerSetFastRead(int twifd) {
	unsigned char command;
	accelerometer_write(twifd, &(command = 0b11), 0x2A, 1); //fast active
}

static void accelerometerSetNormalRead(int twifd) {
	unsigned char command;
	accelerometer_write(twifd, &(command = 0b10), 0x2A, 1); //fast active
}


//check f_read mode before using
static void getAcceration(int twifd, uint16_t* measurementArray) {
	unsigned char data[6];
	accelerometer_read(twifd, data, 0x01, sizeof(data)); //read registers 1-7
	for (int i = 0; i < 3; i++) {
		measurementArray[i] = (data[2*i] << 6) + (data[2*i + 1] >> 2); //shifts MSB and LSB into correct digits
	}
}

//check f_read mode before using
static void getFastAcceration(int twifd, uint16_t* measurementArray) {//8 MSB needs Autoincrement to be fast mode
	unsigned char data[3];
	accelerometer_read(twifd, data, 0x01, sizeof(data));
	for (int i = 0; i < 3; i++) {
		measurementArray[i] = data[i]; 
	}
}

static int accelerometer_init(void)
{
	static int fd = -1;
	fd = open("/dev/i2c-0", O_RDWR);
	if (fd != -1) {
		if (ioctl(fd, I2C_SLAVE_FORCE, ACCELEROMETER_CHIP_ADDRESS) < 0) {
			perror("Accelerometer did not ACK\n");
			return -1;
		}
	}

	return fd;
}



static int accelerometer_read(int twifd, uint8_t* data, uint16_t addr, short int bytes) //raw bits needs to be converted to Gs
{
	struct i2c_rdwr_ioctl_data packets;
	struct i2c_msg msgs[2];

	msgs[0].addr = ACCELEROMETER_CHIP_ADDRESS;
	msgs[0].flags = 0;
	msgs[0].len = 1;
	msgs[0].buf = (char*)&addr;

	msgs[1].addr = ACCELEROMETER_CHIP_ADDRESS;
	msgs[1].flags = I2C_M_RD;
	msgs[1].len = bytes;
	msgs[1].buf = (char*)data;

	packets.msgs = msgs;
	packets.nmsgs = 2;

	if (ioctl(twifd, I2C_RDWR, &packets) < 0) {
		perror("Unable to send data");
		return 1;
	}

	return 0;
}

static int accelerometer_write(int twifd, uint8_t* data, uint16_t addr, short int bytes) //two wire interface file descriptor, array of commands, command register, number of commands
{
	struct i2c_rdwr_ioctl_data packets;
	struct i2c_msg msg;
	uint8_t outdata[128];

	outdata[0] = addr;
	memcpy(&outdata[1], data, bytes);

	msg.addr = ACCELEROMETER_CHIP_ADDRESS;
	msg.flags = 0;
	msg.len = 1 + bytes;
	msg.buf = (char*)outdata;

	packets.msgs = &msg;
	packets.nmsgs = 1;

	if (ioctl(twifd, I2C_RDWR, &packets) < 0) {
		return 1;
	}
	return 0;
}

#endif