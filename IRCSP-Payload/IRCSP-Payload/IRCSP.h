//
//  IRCSP.h
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/5/21.
//

#pragma once
#include "IRCSP.h"
#include "ConcreteIRCSPStates.h"
#include "Accelerometer.h"
#include "TEC.hpp"

#include <stdio.h>
#include <time.h>

// Forward declaration to resolve circular dependency/include
class IRCSPState;

class IRCSP
{
public:
    //telemetry attributes
    float time_elapsed;
    float acceleration;
    float t_sbc;
    float t_ircsp;
    float dataspace;
    float PID_target;
    
    //State switching parameters
    float TAKEOFF_ACCEL = 1.2;
    float DECENT_ACCEL = 3;
    float CRUISE_ACCEL = 1.1;
    float PREFLIGHT_TIME = 10;
    float MIN_DATASPACE  = 1;
    
    void check_telemetry(time_t, Accelerometer&,TEC&);
    void set_PID(long);
    
    //State Functions
    IRCSP();
    inline IRCSPState* getCurrentState() const { return currentState; }
    void toggle();
    void setState(IRCSPState& newState);

private:
    // IRCSPState here is now a class
    IRCSPState* currentState;
    
    
};



