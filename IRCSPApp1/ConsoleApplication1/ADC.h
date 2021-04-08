#pragma once
#ifndef ADC_H
#define	ADC_H
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
#define ADC_CHIP_ADDRESS 0x54

class ADC
{
public:
	int twifd;
	short measurementArray[5];
	float voltages[5]; //implement voltage to temperature outside class
	float vref = 5; //5 volt
	ADC();
	ADC(int twifd);
	~ADC();
	void getADC();
	short getADC(char);
	static int ADC_init();
	static int ADC_read(int twifd, uint8_t* data, uint16_t addr, int bytes);
	static int ADC_write(int twifd, uint8_t* data, uint16_t addr, int bytes);
private:

};

ADC::ADC()
{
	twifd = ADC_init();
}

ADC::ADC(int twifd) {
	this->twifd = twifd;
}

ADC::~ADC()
{
	close(twifd);
}

int ADC::ADC_init(){
static int fd = -1;
fd = open("/dev/i2c-0", O_RDWR);
if (fd != -1) {
	if (ioctl(fd, I2C_SLAVE_FORCE, ADC_CHIP_ADDRESS) < 0) {
		perror("SiLabs did not ACK\n");
		return -1;
	}
}

return fd;
}

int ADC::ADC_read(int twifd, uint8_t* data, uint16_t addr, int bytes)
{
	struct i2c_rdwr_ioctl_data packets;
	struct i2c_msg msgs[2];
	char busaddr[2];

	busaddr[0] = ((addr >> 8) & 0xff);
	busaddr[1] = (addr & 0xff);

	msgs[0].addr = ADC_CHIP_ADDRESS;
	msgs[0].flags = 0;
	msgs[0].len = 2;
	msgs[0].buf = busaddr;

	msgs[1].addr = ADC_CHIP_ADDRESS;
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

int ADC::ADC_write(int twifd, uint8_t* data, uint16_t addr, int bytes)
{
	struct i2c_rdwr_ioctl_data packets;
	struct i2c_msg msg;
	uint8_t outdata[4096];

	/* Linux only supports 4k transactions at a time, and we need
	 * two bytes for the address */
	//assert(bytes <= 4094);

	outdata[0] = ((addr >> 8) & 0xff);
	outdata[1] = (addr & 0xff);
	memcpy(&outdata[2], data, bytes);

	msg.addr = ADC_CHIP_ADDRESS;
	msg.flags = 0;
	msg.len = 2 + bytes;
	msg.buf = (char*)outdata;

	packets.msgs = &msg;
	packets.nmsgs = 1;

	if (ioctl(twifd, I2C_RDWR, &packets) < 0) {
		return 1;
	}
	return 0;
}

void ADC::getADC() {
	uint8_t buf[10];
	short reg = 1280 + 14; // ADC regs are 1280-1535 (0x50-5F) gotten from source, 10bits each, RE
	ADC_read(twifd, buf, reg, 10);
	for (signed char i = 4; i >= 0; i--) {
		measurementArray[i] = (buf[2 * i + 1] << 7) + buf[2 * i];
		voltages[i] = (measurementArray[i] * vref) / pow(2,10);
	}

}


#endif
