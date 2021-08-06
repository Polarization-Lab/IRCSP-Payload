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


#include "IRCSP.h"
#include "ConcreteIRCSPStates.h"
#include <iostream>
#include <stdexcept>

typedef enum SBCstate_enum { boot, preflight, takeoff, cruising, shutdown } SBCstate; //SBC states

int main(void)
{
    //Record Start Time
    long bootTime = time(NULL), currentTime, lastAccelCheck = bootTime; // stores epoch time;
    
    //Assign volatile memory
    volatile SBCstate lastState, sbcState = boot;
    
    //Generate IRCSP Class object
    IRCSP ircsp;
    
    for(int i = 0; i<10; i++)
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
                ircsp.check_telemetry(bootTime);
               
                std::cout<< "Time elapsed since boot " << ircsp.time_elapsed << " s \n";
                ircsp.acceleration = 1.5;
                if (ircsp.time_elapsed > 10 or ircsp.acceleration > 1.25 )
                {
                    sbcState = takeoff;
                    ircsp.toggle();
                    sleep(1);
                }
            }
                
            case takeoff:
            {
                std::cout<< "Acceleration =  " << ircsp.acceleration << " G \n";
                if (ircsp.time_elapsed > 10 or ircsp.acceleration < 1.25 )
                {
                    sbcState = cruising;
                    ircsp.toggle();
                    sleep(1);
                }
            }
                
            case cruising:
            {
                ircsp.acceleration = 1;
                if (ircsp.time_elapsed > 10 or ircsp.acceleration < 1.25 )
                {
                    sbcState = cruising;
                    ircsp.toggle();
                    sleep(1);
                }
            }
        }
    }
    return 0;
}
