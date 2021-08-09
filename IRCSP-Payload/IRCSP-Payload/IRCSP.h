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
#include "NTCThermistorDecoder.h"
#include "ADC.h"

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
    float cam1_t;
    float cam2_t;
    float temperatures[5];
    bool adcChannels[5] = { 1 };
    const float NTCparam[4][5] = { {4.46}, { 10700 }, { 25 + 273}, { 10000 } }; //source voltage, resistors, reference Temp, thermistor reference temperature, thermistor sensitivty
    const float NKA103C1R1CCoef[5][4] = { { 3.3539438E-03, 2.5646095E-04, 2.5158166E-6, 1.0503069E-07} };
    
    
    //State switching parameters
    float TAKEOFF_ACCEL = 1.2;
    float DECENT_ACCEL = 3;
    float CRUISE_ACCEL = 1.1;
    float PREFLIGHT_TIME = 10;
    float MAX_DATA  = 1000;
    float MIN_TEMP = 10;
    int wait_time  = 5;
    int MAX_TIME = 30; //in seconds

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



