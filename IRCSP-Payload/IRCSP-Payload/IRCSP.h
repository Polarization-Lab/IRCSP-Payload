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
    float humidity;
    float dataspace;
    float PID_target;
    
    
    //State switching parameters
    float TAKEOFF_ACCEL = 1.2;
    float DECENT_ACCEL = 3;
    float CRUISE_ACCEL = 1.1;
    float PREFLIGHT_TIME = 10;
    float MAX_DATA  = 100;
    int   sampling = 60; //interval to take telemetry
    
    //filepaths
    std::string logPath = "/Users/kirahart/Documents/Github/IRSCP-Payload/IRCSP-Payload/data/log.txt";
    std::string telemetryPath ="/Users/kirahart/Documents/Github/IRSCP-Payload/IRCSP-Payload/data/telemetry.txt";
    std::string dataPath ="/Users/kirahart/Documents/Github/IRSCP-Payload/IRCSP-Payload/data/";
    std::string ircspPath = "/Users/kirahart/Documents/Github/IRSCP-Payload/IRCSP-Payload/image_capture.py";
    
    void check_telemetry(time_t, Accelerometer&,TEC&);
    void set_PID(long);
    
    //State Functions
    IRCSP();
    inline IRCSPState* getCurrentState() const { return currentState; };
    void toggle();
    void setState(IRCSPState& newState);
    int GetStdoutFromCommand(std::string);
    
private:
    // IRCSPState here is now a class
    IRCSPState* currentState;
    
    
};



