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
#include <fstream>
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
    time_t bootTime = time(NULL), currentTime,start; // stores epoch time;
    
    //Initial State is BOOT, update upon state change
    SBCstate  sbcState = boot;
    
    //Generate Instrument Class Objects
    IRCSP ircsp;
    Accelerometer accelerometer;
    TEC tec;
    
    //Gereate logging objects and files in append mode
    std::fstream log;
    std::fstream telemetry;
    log.open ("/Users/kirahart/Documents/Github/IRSCP-Payload/IRCSP-Payload/log.txt",std::fstream::app);
    telemetry.open ("/Users/kirahart/Documents/Github/IRSCP-Payload/IRCSP-Payload/telemetry.txt",std::fstream::app);
    
    //declare start of loop
    currentTime = time(NULL);
    log << std::ctime(&currentTime) << " Main Function Initiated \n" ;
    
    //Get power access to USB ports
    //system("echo 45 > /sys/class/gpio/export"); //Enables software control of USB power
    //system("echo \"out\" > /sys/class/gpio/gpio45/direction"); // Default USB power is off in this mode.
    //system("echo 1 > /sys/class/gpio/gpio45/value"); //turns USB power on
    
    //Other Main funct. variables
    int childPid , childStatus;
   
    //begin time to save telemery
    time_t t;
    t = time(NULL);
    
    for(int i = 0; i<200; i++)
    {
        long double timeSpent =   ( time(NULL) - t ) ;
        
        if(timeSpent > ircsp.sampling){
            currentTime = time(NULL);
            ircsp.check_telemetry(bootTime,accelerometer,tec);
            
            telemetry << std::setprecision(4) << std::fixed; //set some precision for nice format
            telemetry << std::setw(7) << strtok(std::ctime(&currentTime), "\n") << " ";
            telemetry << std::setw(4) << ircsp.acceleration << " ";
            telemetry << std::setw(4) << ircsp.t_sbc << " ";
            telemetry << std::setw(4) << ircsp.t_ircsp  << " ";
            telemetry << std::setw(4) << ircsp.humidity << " ";
            telemetry << '\n';
            
            t = time(NULL);
        }

        switch (sbcState) //state handler
        {
            case boot:
                currentTime = time(NULL);
                log << std::ctime(&currentTime) << " System Booting \n" ;
                
                if (bootTime != .1)//boot check //do once while leaving
                {   sbcState = boot;
                    //print message to log
                    ircsp.check_telemetry(bootTime,accelerometer,tec);
                    currentTime = time(NULL);
                    
                    //toggle to next state
                    if(ircsp.t_ircsp < 0){//check if at altitude
                        sbcState = cruising;
                        log << std::ctime(&currentTime) << " Cruising \n";
                        //system("echo 1 > /sys/class/gpio/gpio45/value"); //turns USB power on
                    }
                    else{
                        sbcState = preflight;
                        log << std::ctime(&currentTime) << " Entering Preflight \n";
                    }
                    ircsp.toggle();
                     
                    sleep(1);
                break;
            }
            
            case preflight:
                
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                sbcState = preflight;
                
                //system("echo 0 > /sys/class/gpio/gpio45/value"); //turns USB power off
                
                //SWITCH CONDITION
                if (ircsp.time_elapsed > ircsp.PREFLIGHT_TIME || ircsp.acceleration > ircsp.TAKEOFF_ACCEL )
                {

                    //system("echo 1 > /sys/class/gpio/gpio45/value"); //turns USB power on
                    sleep(10);
                    
                    sbcState = takeoff;
                    ircsp.toggle();
                    
                    currentTime = time(NULL);
                    log << std::ctime(&currentTime) << " Entering TakeOff \n"  ;
                    log << ircsp.acceleration <<" " << ircsp.t_sbc <<" " << ircsp.t_ircsp<<" " << ircsp.humidity << "\n"  ;
                    
                    
                }
                break;

                
            case takeoff:
                //system("echo 1 > /sys/class/gpio/gpio45/value"); //turns USB power on
                sleep(10);
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                
                /*if ((childPid = fork()) == 0)
                {
                execlp("/Users/kirahart/Documents/Github/IRSCP-Payload/IRCSP-Payload/image_capture.py","image_capture.py");
                }
                */
                 
                sbcState = takeoff;
                //SWITCH CONDITION
                if (ircsp.acceleration < ircsp.CRUISE_ACCEL)
                {
                    sbcState = cruising;
                    ircsp.toggle();
                    
                    log << std::ctime(&currentTime) << " Cruising \n"  ;
                    log << ircsp.acceleration <<" " << ircsp.t_sbc <<" " << ircsp.t_ircsp<<" " << ircsp.humidity;
                }
                break;


                
            case cruising:
                sleep(1);
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                sbcState = cruising;
                
                //SWITCH CONDITION
                if (ircsp.acceleration > ircsp.DECENT_ACCEL )
                {
                    sbcState = falling;
                    ircsp.toggle();
                    
                    log << std::ctime(&currentTime) << " Falling \n"  ;
                    log << ircsp.acceleration <<" " << ircsp.t_sbc <<" " << ircsp.t_ircsp<<" " << ircsp.humidity << " \n";
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
                //system("ts7800ctl -s 3600"); // put SBC in sleep mode
                break;
                
        }
    }
    
    log.close();
    telemetry.close();
    
    
    return 0;
}
