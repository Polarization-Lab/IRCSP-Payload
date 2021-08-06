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



typedef enum SBCstate_enum { boot, preflight, takeoff, cruising, falling, shutdown } SBCstate; //SBC states

// -----GLOBAL VARIABLES---------

int main(void)
{
    //Record Start Time
    time_t bootTime = time(NULL),  lastAccelCheck = bootTime; // stores epoch time;
    
    //Assign volatile memory
    volatile SBCstate  sbcState = boot;
    
    //Generate Instrument Class Objects
    IRCSP ircsp;
    Accelerometer accelerometer;
    TEC tec;
    
    //Other Main funct. variables
    int childPid, childStatus;

    
    for(int i = 0; i<20; i++)
    {
        switch (sbcState) //state handler
        {
            case boot:
            {
                fprintf(stderr, "Booting \n");
                if (true && bootTime != .1)//boot check //do once while leaving
                {
                    sbcState = preflight;
                    ircsp.toggle();
                    sleep(1);
                }
                break;
            }
            
            
            case preflight:
            {
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                ircsp.acceleration = 1.5;
                
                //SWITCH CONDITION
                if (ircsp.time_elapsed > ircsp.PREFLIGHT_TIME or ircsp.acceleration > ircsp.TAKEOFF_ACCEL )
                {
                    std::cout<< "Acceleration =  " << ircsp.acceleration << " G \n";
                    sbcState = takeoff;
                    ircsp.toggle();
                    
                }
            }
                
            case takeoff:
            {
                //SWITCH CONDITION
                if (ircsp.acceleration < ircsp.CRUISE_ACCEL)
                {
                    sbcState = cruising;
                    ircsp.toggle();
                }
            }
                
            case cruising:
            {
                ircsp.acceleration = 1;
                if (i >10)
                    ircsp.acceleration = 4;
                
                //SWITCH CONDITION
                if (ircsp.acceleration > ircsp.DECENT_ACCEL )
                {
                    sbcState = shutdown;
                    ircsp.toggle();
                }
            }
                
            case falling:
            {
                ircsp.acceleration = 1;
                
                //SWITCH CONDITION
                if (ircsp.dataspace < ircsp.MIN_DATASPACE )
                {
                    sbcState = shutdown;
                    ircsp.toggle();
                }
            }
                
            case shutdown:
            {//ircsp.check_telemetry(bootTime,accelerometer,tec);
            }
        }
    }
    return 0;
}
