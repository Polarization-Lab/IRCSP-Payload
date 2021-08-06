//
//  TEC.cpp
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/6/21.
//

#include "TEC.hpp"

#include <stdio.h>
#include <cmath>


TEC::TEC()
{
    set_temp = 1;
}

TEC::TEC(int twifd) {
    this->twifd = twifd;
}

void TEC::setTEC(float temp) {
    set_temp = temp;
}

TEC::~TEC()
{
}
