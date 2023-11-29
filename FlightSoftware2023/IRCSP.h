//
//  IRCSP.h
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/5/21.
//

#pragma once
#include "IRCSPState.h"
#include "ConcreteIRCSPStates.h"


#include <string>
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
    float t_amb;
    float t_sbc;
    float amb_humidity;
    float amb_pressure;
    float t_elec;
    float elec_humidity;
    float elec_pressure;
    float t_ircsp;
    float ircsp_humidity;
    float ircsp_pressure;
    float dataspace;
    float voltage;
    float t_cam1;
    float t_cam2;
    float t_cam3;
    float thermVal;
    float contextVal;
    float lensVal;
    float therm_temp;
    float context_temp;
    float lens_temp;    
    float heat_temp;
    float heat_V;    

    //State switching parameters
    float TAKEOFF_ACCEL = .9;;
    float DECENT_ACCEL = 3;
    float CRUISE_ACCEL = 1.1;
    float PREFLIGHT_TIME = 10;
    float MAX_DATA  = 100000000;
    float MIN_TEMP = 10;
    int wait_time  = .1;
    int MAX_TIME = 10000; //in seconds
    int FLIGHT_ALT = 122; //mbar

    int sampling = 10; //interval to take telemetry
    
    //filepaths
    std::string logPath = "/mnt/sdcard/image_data/log.txt";
    std::string telemetryPath ="/mnt/sdcard/image_data/telemetry.csv";
    std::string dataPath ="/mnt/sdcard/image_data/";
    std::string ircspPath = "/home/IRCSP-Payload/image_capture.py";
    
    void check_telemetry(time_t);
    
    //State Functions
    IRCSP();
    inline IRCSPState* getCurrentState() const { return currentState; };
    void toggle();
    void setState(IRCSPState & newState);
    int GetStdoutFromCommand(std::string);
    
private:
    // IRCSPState here is now a class
    IRCSPState* currentState;
    
    
};
