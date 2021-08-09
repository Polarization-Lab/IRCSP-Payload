//
//  ConcreteIRCSPStates.cpp
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/5/21.
//

#include "ConcreteIRCSPStates.h"

void Boot::toggle(IRCSP* ircsp)
{
    if (ircsp -> time_elapsed < ircsp->PREFLIGHT_TIME ) {
        // Boot -> Preflight (TODO: change to check for stored data)
        ircsp->setState(Preflight::getInstance());}
    if (ircsp -> cam1_t < ircsp-> MIN_TEMP || ircsp -> cam2_t < ircsp-> MIN_TEMP ){
        // Boot -> Cruising
        ircsp->setState(Cruising::getInstance());}
         
}

IRCSPState& Boot::getInstance()
{
    static Boot singleton;
    return singleton;
}


void Preflight::toggle(IRCSP* ircsp)
{
     // Preflight -> Takeoff
    ircsp->setState(Takeoff::getInstance());
}

IRCSPState& Preflight::getInstance()
{
    static Preflight singleton;
    return singleton;
}


void Takeoff::toggle(IRCSP* ircsp)
{
    if (ircsp-> acceleration < ircsp-> CRUISE_ACCEL) {
        // Takeoff -> Crusing
        ircsp->setState(Cruising::getInstance());}
    else  {
        // Takeoff -> Shutdown
        ircsp->setState(Shutdown::getInstance());}
         
}
IRCSPState& Takeoff::getInstance()
{
    static Takeoff singleton;
    return singleton;
}

void Cruising::toggle(IRCSP* ircsp)
{
    if (ircsp-> acceleration > ircsp-> DECENT_ACCEL) {
    // Takeoff -> Crusing
        ircsp->setState(Cruising::getInstance());}
    if (ircsp-> dataspace > ircsp-> MAX_DATA) {
        // Takeoff -> Shutdown
        ircsp->setState(Shutdown::getInstance());}
}

IRCSPState& Cruising::getInstance()
{
    static Cruising singleton;
    return singleton;
}

void Falling::toggle(IRCSP* ircsp)
{
    // Falling -> Shutdown
    ircsp->setState(Shutdown::getInstance());
}

IRCSPState& Falling::getInstance()
{
    static Falling singleton;
    return singleton;
}


void Shutdown::toggle(IRCSP* ircsp)
{
    // Shutdown -> Boot
    ircsp->setState(Boot::getInstance());
}

IRCSPState& Shutdown::getInstance()
{
    static Shutdown singleton;
    return singleton;
}
