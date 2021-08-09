#pragma once
#ifndef ACCELEROMETER_H
#define    ACCELEROMETER_H
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
	int fullscale = 4; //g range
	float gValues[3];
    float total_accel;
	

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
    
	
	
private:
	
    void getRawAcceleration(); //consider moving to private
    void getFastRawAcceleration(); //consider moving to private
    bool OAE = 0; //Freefall/motion dection configuration
    uint8_t FF_MT_threshold = 0b0;
    uint8_t zyxEFE = 0b100;
    uint8_t interupt;
};

#endif


