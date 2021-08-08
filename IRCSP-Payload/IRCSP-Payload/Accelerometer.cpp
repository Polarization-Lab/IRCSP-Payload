//
//  Accelerometer.cpp
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/6/21.
//
#ifndef ACCELEROMETER_H
#define    ACCELEROMETER_H
#include <stdio.h>
#include "Accelerometer.h"
#include <cmath>


Accelerometer::Accelerometer()
{
    twifd = 1;
}

Accelerometer::Accelerometer(int twifd) {
    this->twifd = twifd;
}

void Accelerometer::getAcceleration() {
    float a = 0;
    for (int i = 0; i < 3; i++) {
        gValues[i] = (float) rand()/RAND_MAX;
        a = a + pow((float) rand()/RAND_MAX +.1,2);
    total_accel = sqrt(a);
    }

}

Accelerometer::~Accelerometer()
{
}

#endif
