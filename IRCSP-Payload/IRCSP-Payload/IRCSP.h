//
//  IRCSP.h
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/5/21.
//

#pragma once
#include "IRCSPState.h"
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
    
    void check_telemetry(long);
    
    //State Functions
    IRCSP();
    inline IRCSPState* getCurrentState() const { return currentState; }
    void toggle();
    void setState(IRCSPState& newState);

private:
    // IRCSPState here is now a class
    IRCSPState* currentState;
};
