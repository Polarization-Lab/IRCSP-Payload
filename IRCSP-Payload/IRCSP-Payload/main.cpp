//
//  main.cpp
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/4/21.
//
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include <cstdio>
#include <cmath>
#include <time.h>
#include <sys/mman.h>
//#include <linux/pci.h>
#include <unistd.h>
#include <termios.h>
#include <iostream>
#include <stdexcept>
#include <Python/Python.h>



#include "IRCSP.h"
#include "ConcreteIRCSPStates.h"



enum SBCstate { boot, preflight, takeoff, cruising, falling, shutdown } ; //SBC states

// -----GLOBAL VARIABLES---------

int main(void)
{
    //Record Start Time
    time_t bootTime = time(NULL), currentTime,  lastAccelCheck = bootTime; // stores epoch time;
    
    //Initial State is BOOT, update upon state change
    SBCstate  sbcState = boot;
    
    //Generate Instrument Class Objects
    IRCSP ircsp;
    Accelerometer accelerometer;
    TEC tec;
    
    //Other Main funct. variables
    int childPid , childStatus;
    FILE * logFile = nullptr;
    FILE * telemetryFile;
   
    logFile = fopen ("/Users/kirahart/Documents/Github/IRSCP-Payload/IRCSP-Payload/log.txt","w");
    telemetryFile = fopen ("/Users/kirahart/Documents/Github/IRSCP-Payload/IRCSP-Payload/telemetry.txt","w");
    for(int i = 0; i<10; i++)
    {
        std::cout << sbcState;
        switch (sbcState) //state handler
        {
            case boot:
                if (bootTime != .1)//boot check //do once while leaving
                {   sbcState = boot;
                    //print message to log
                    ircsp.check_telemetry(bootTime,accelerometer,tec);
                  
                    //toggle to next state
                    sbcState = preflight;
                    ircsp.toggle();
                    sleep(1);
                break;
            }
            
            
            
            case preflight:
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                sbcState = preflight;
                //SWITCH CONDITION
                if (ircsp.time_elapsed > ircsp.PREFLIGHT_TIME || ircsp.acceleration > ircsp.TAKEOFF_ACCEL )
                {

                    sbcState = takeoff;
                    ircsp.toggle();
                }
                break;

                
            case takeoff:
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                
                //execlp("/Users/kirahart/Documents/Github/IRSCP-Payload/IRCSP-Payload/image_capture.py","image_capture.py");

                sbcState = takeoff;
                //SWITCH CONDITION
                if (ircsp.acceleration < ircsp.CRUISE_ACCEL)
                {
                    sbcState = cruising;
                    ircsp.toggle();
                }
                break;


                
            case cruising:
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                sbcState = cruising;
                
                //SWITCH CONDITION
                if (ircsp.acceleration > ircsp.DECENT_ACCEL )
                {
                    sbcState = shutdown;
                    ircsp.toggle();
                }
                break;

                
            case falling:
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                //SWITCH CONDITION
                if (ircsp.dataspace < ircsp.MIN_DATASPACE )
                {
                    sbcState = shutdown;
                    ircsp.toggle();
                }
                break;
            
            case shutdown:
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                break;
                
        }
    }
    
    fclose(logFile) ;
    fclose(telemetryFile);
    return 0;
}
