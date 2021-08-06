//
//  ConcreteIRCSPStates.cpp
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/5/21.
//

#include "ConcreteIRCSPStates.h"

void Boot::toggle(IRCSP* ircsp)
{
    if (ircsp -> time_elapsed < 10 ) {
        // Boot -> Preflight
        ircsp->setState(Preflight::getInstance());}
    else  {
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
    if (ircsp -> acceleration < 1.25) {
        // Preflight -> Preflight
        ircsp->setState(Preflight::getInstance());}
    else  {
        // Preflight -> Takeoff
        ircsp->setState(Takeoff::getInstance());}
         
}

IRCSPState& Preflight::getInstance()
{
    static Preflight singleton;
    return singleton;
}

void Takeoff::toggle(IRCSP* ircsp)
{
    if (ircsp-> acceleration < 1.25) {
        // Takeoff -> Crusing
        ircsp->setState(Cruising::getInstance());}
    else  {
        // Takeoff -> Shutdown
        ircsp->setState(Takeoff::getInstance());}
         
}
IRCSPState& Takeoff::getInstance()
{
    static Takeoff singleton;
    return singleton;
}

void Cruising::toggle(IRCSP* ircsp)
{ 
    // Cruising -> Shutdown
    ircsp->setState(Shutdown::getInstance());
}

IRCSPState& Cruising::getInstance()
{
    static Cruising singleton;
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
