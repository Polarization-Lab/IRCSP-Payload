//
//  IRCSP.cpp
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/5/21.
//

#include "IRCSP.h"
#include "ConcreteIRCSPStates.h"

IRCSP::IRCSP()
{
    // All lights are initially turned off
    currentState = &Boot::getInstance();
}

void IRCSP::setState(IRCSPState& newState)
{
    currentState->exit(this);  // do stuff before we change state
    currentState = &newState;  // actually change states now
    currentState->enter(this); // do stuff after we change state
}

void IRCSP::toggle()
{
    // Delegate the task of determining the next state to the current state
    currentState->toggle(this);
}

void IRCSP::check_telemetry (long bootTime)
{
    time_elapsed = time(NULL) - bootTime;
    acceleration = 1;
    t_sbc = 1;
    t_ircsp = 1;
    dataspace =1;
}

