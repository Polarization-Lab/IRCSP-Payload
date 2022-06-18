#pragma once
#ifndef ACCELEROMETER_H
#define	ACCELEROMETER_H
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
#include <cmath>
#define ACCELEROMETER_CHIP_ADDRESS 0x1c
#define DEBOUNCE_COUNT 0b00001111

class Accelerometer
{
public:
	int twifd; //points to i2c-dev file
	signed short measurementArray[3]; //records x,y,z
	bool fRead = false; //fast read mode
	int fullscale = 2; //g range
	float gValues[3];
	

	Accelerometer(); //creates new object
	Accelerometer(int twifd);
	~Accelerometer(); //destorys object
	
	static int accelerometer_init(void); //gets I2C file descriptor, establishes comms with accelerometer
	static int accelerometer_read(int twifd, uint8_t* data, uint16_t addr, short int bytes);
	static int accelerometer_write(int twifd, uint8_t* data, uint16_t addr, short int bytes);
	static int accelerometer_write(int twifd, uint8_t data, uint16_t addr);
	
	void setFF_MTN_THS_CFG(uint8_t data, uint8_t axis, bool OAE); //use binary input to set accelerometer threshold for motion detect & for freefall mode 
	void setMotionFreefallInterupt(float g, uint8_t axis, bool MotionDetection); //use g value to set accelerometer threshold
	void setDebounceCount(uint8_t count);
	bool checkMotionInteruptFlag(uint8_t* flags); //gets the FF_MT_SRC freefall/motion source register returns true if EA is raised

	void setTransientInterupt(uint8_t data, uint8_t axis); //use raw //define
	void setTransientInterupt(float g, uint8_t axis); //use gs //define
	bool checkTransientInteruptFlag(); //define
	
	void accelerometer_reset();
	void setStandby();
	void setActive();
	void setFastRead();
	void setNormalRead();
	void getAcceleration(); //gets converted acceleration into gValues
	void getRawAcceleration(); //consider moving to private
	void getFastRawAcceleration(); //consider moving to private
	
	//void sleepAccelerometer(int hr, int min, int sec); //no
private:
	bool OAE = 0; //Freefall/motion dection configuration
	uint8_t FF_MT_threshold = 0b0;
	uint8_t zyxEFE = 0b100;
	uint8_t interupt;
};

Accelerometer::Accelerometer()
{
	twifd = accelerometer_init();
	accelerometer_reset();
	setDebounceCount((uint8_t)DEBOUNCE_COUNT);
}

Accelerometer::Accelerometer(int twifd) {
	this->twifd = twifd;
	accelerometer_reset();
	setDebounceCount((uint8_t)DEBOUNCE_COUNT);
}

Accelerometer::~Accelerometer()
{
	close(twifd);
}


int Accelerometer::accelerometer_init(void)
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

int Accelerometer::accelerometer_read(int twifd, uint8_t* data, uint16_t addr, short int bytes) //raw bits needs to be converted to Gs
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

int Accelerometer::accelerometer_write(int twifd, uint8_t* data, uint16_t addr, short int bytes) //two wire interface file descriptor, array of commands, command register, number of commands
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

int Accelerometer::accelerometer_write(int twifd, uint8_t data, uint16_t addr) {
	struct i2c_rdwr_ioctl_data packets;
	struct i2c_msg msg;
	uint8_t outdata[2];

	outdata[0] = addr;
	outdata[1] = data;

	msg.addr = ACCELEROMETER_CHIP_ADDRESS;
	msg.flags = 0;
	msg.len = 1 + 1;
	msg.buf = (char*)outdata;

	packets.msgs = &msg;
	packets.nmsgs = 1;

	if (ioctl(twifd, I2C_RDWR, &packets) < 0) {
		return 1;
	}
	return 0;
}

void Accelerometer::setFF_MTN_THS_CFG(uint8_t threshold, uint8_t axis, bool _OAE)
{
	FF_MT_threshold = threshold;
	zyxEFE = axis & 0b111;
	OAE = _OAE;
	uint8_t CFG[4];
	CFG[0] = (uint8_t)((1 << 7) | (OAE << 6) | (zyxEFE) << 3);
	CFG[1] = 0;
	CFG[2] = FF_MT_threshold & ~(0b10000000); //set threshold register
	CFG[3] = DEBOUNCE_COUNT & 0xFF; //set debounce counter mode to 0, set to decrement on no-detect
	setStandby();
	accelerometer_write(twifd, CFG, 0x15, 4); //0x15 can only be edited in stby mode
	setActive();
	accelerometer_read(twifd, &interupt, 0x16, 1); //clears the 0x16: FF_MT_SRC freefall/motion source register
}

void Accelerometer::setMotionFreefallInterupt(float g, uint8_t axisZYX, bool MotionDetection) {
	uint8_t bits = (uint8_t) floor(g / .063);
	setFF_MTN_THS_CFG(bits, axisZYX, MotionDetection);
}

void Accelerometer::setDebounceCount(uint8_t count) {
	accelerometer_write(twifd, count, 0x18);
}

bool Accelerometer::checkMotionInteruptFlag(uint8_t* flags) {
	accelerometer_read(twifd, &interupt, 0x16, 1);
	if (flags != NULL)
		*flags = interupt;
	return (interupt)&0b10000000;
}

void Accelerometer::setTransientInterupt(uint8_t data, uint8_t axis) {
	axis &= 0b111;
	accelerometer_write(twifd, (uint8_t)((1 << 4) | (axis << 1)), 0x1D);
	data &= ~(0b10000000);
	accelerometer_write(twifd, data, 0x1F);
	accelerometer_write(twifd, (uint8_t)DEBOUNCE_COUNT, 0x20);
}

void Accelerometer::setTransientInterupt(float g, uint8_t axis) {
	setTransientInterupt((uint8_t)floor(g / .063), axis);
}

void Accelerometer::accelerometer_reset() {
	uint8_t command;
	accelerometer_read(twifd, &command, 0X2A, 1); //get ctl2 flags
	accelerometer_write(twifd, &(command |= 0b01000000), 0x2B, 1); //set reset int cntl reg 2
	usleep(100000);
	accelerometer_write(twifd, &(command |= 0b1), 0x2A, 1); //set active in ctrl reg 
}

void Accelerometer::setStandby() {
	uint8_t CTRL_REG1;
	accelerometer_read(twifd, &CTRL_REG1, 0X2A, 1);
	CTRL_REG1 &= ~1;
	accelerometer_write(twifd, CTRL_REG1, 0X2A);
}

void Accelerometer::setActive() {
	uint8_t CTRL_REG1;
	accelerometer_read(twifd, &CTRL_REG1, 0X2A, 1);
	CTRL_REG1 |= 1;
	accelerometer_write(twifd, CTRL_REG1, 0X2A);
}

void Accelerometer::setFastRead() {
	accelerometer_write(twifd, 0b11, 0x2A); //fast active
}

void Accelerometer::setNormalRead() {
	accelerometer_write(twifd, 0b10, 0x2A); //normal active
}

//check f_read mode before using
void Accelerometer::getRawAcceleration() {
	unsigned char data[6];
	accelerometer_read(twifd, data, 0x01, sizeof(data)); //read registers 1-7
	for (int i = 0; i < 3; i++) {
		measurementArray[i] = (signed short)((data[2 * i] << 8) + (data[2 * i + 1])); //shifts MSB and LSB into correct digits, Value = FullScale Range/2^13
	}
}

//check f_read mode before using
void Accelerometer::getFastRawAcceleration() {//8 MSB needs Autoincrement to be fast mode
	unsigned char data[3];
	accelerometer_read(twifd, data, 0x01, sizeof(data));
	for (int i = 0; i < 3; i++) {
		measurementArray[i] = (signed short)(data[i] << 8); //value = FullScale Range/2^7 
	}
}

void Accelerometer::getAcceleration() {
	if (fRead) {
		getFastRawAcceleration();
	}
	else
	{
		getRawAcceleration();
	}
	for (int i = 0; i < 3; i++) {
		gValues[i] = measurementArray[i] * fullscale / pow(2, 15);
	}

}

#endif
