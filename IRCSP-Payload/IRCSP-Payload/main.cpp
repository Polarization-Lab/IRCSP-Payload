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
#include<sstream>



#include "IRCSP.h"
#include "ConcreteIRCSPStates.h"



enum SBCstate { boot, preflight, takeoff, cruising, falling, shutdown } ; //SBC states

int main(void)
{
    //Record Start Time
    time_t bootTime = time(NULL), currentTime; // stores epoch time;
    
    //Initial State is BOOT, update upon state change
    SBCstate  sbcState = boot;
    
    //Generate Instrument Class Objects
    IRCSP ircsp;
    Accelerometer accelerometer;
    TEC tec;
    
    //Gereate logging objects and files in append mode
    std::fstream log;
    std::fstream telemetry;
    log.open (ircsp.logPath,std::fstream::app);
    telemetry.open (ircsp.telemetryPath,std::fstream::app);
    
    //declare start of loop
    currentTime = time(NULL);
    log << std::ctime(&currentTime) << " Main Function Initiated \n" ;
    log.close();
    telemetry.close();
    
    //Get power access to USB ports
    //system("echo 45 > /sys/class/gpio/export"); //Enables software control of USB power
    //system("echo \"out\" > /sys/class/gpio/gpio45/direction"); // Default USB power is off in this mode.
    //system("echo 1 > /sys/class/gpio/gpio45/value"); //turns USB power on
    
    //Other Main funct. variables
    int childPid , childStatus;
    
   
    //begin time to save telemery
    time_t t;
    t = time(NULL);


    for(int i = 0; i<1000; i++)
        
    {
        log.open (ircsp.logPath,std::fstream::app);
        telemetry.open (ircsp.telemetryPath,std::fstream::app);
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
                        sleep(10);
                        
                        if ((childPid = fork()) == 0)
                        {
                        std::cout << "fork at preflight \n";
                        execlp("/Users/kirahart/opt/anaconda3/bin/python", "python","/Users/kirahart/Documents/Github/IRSCP-Payload/IRCSP-Payload/image_capture.py", NULL);
                        }
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
                    
                    if ((childPid = fork()) == 0)
                    {
                    std::cout << "fork at preflight \n";
                    execlp("/Users/kirahart/opt/anaconda3/bin/python", "python","/Users/kirahart/Documents/Github/IRSCP-Payload/IRCSP-Payload/image_capture.py", NULL);
                    }
                    
                    
                }
                break;

                
            case takeoff:
                ircsp.check_telemetry(bootTime,accelerometer,tec);
 
                sbcState = takeoff;
                //SWITCH CONDITION
                if (ircsp.acceleration < ircsp.CRUISE_ACCEL || ircsp.dataspace > ircsp.MAX_DATA)
                {
                    sbcState = cruising;
                    ircsp.toggle();
                    
                    log << std::ctime(&currentTime) << " Cruising \n"  ;
                    log << ircsp.acceleration <<" " << ircsp.t_sbc <<" " << ircsp.t_ircsp<<" " << ircsp.humidity<< " \n";
                }
                break;


                
            case cruising:
    
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
                if (ircsp.dataspace > ircsp.MAX_DATA)
                {
                    sbcState = shutdown;
                    ircsp.toggle();
                    
                    log << std::ctime(&currentTime) << " Data Max Reached, Shutting Down \n"  ;
                    log << ircsp.acceleration <<" " << ircsp.t_sbc <<" " << ircsp.t_ircsp<<" " << ircsp.humidity << " \n";
                }
                break;

                
            case falling:
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                //SWITCH CONDITION
                if (ircsp.dataspace > ircsp.MAX_DATA )
                {
                    log << std::ctime(&currentTime) << " Data Max Reached, Shutting Down \n"  ;
                    log << ircsp.acceleration <<" " << ircsp.t_sbc <<" " << ircsp.t_ircsp<<" " << ircsp.humidity << " \n";
                    sbcState = shutdown;
                    ircsp.toggle();
                }
                break;
            
            case shutdown:
                //system("ts7800ctl -s 3600"); // put SBC in sleep mode
                break;
                
        }
        log.close();
        telemetry.close();
    }
    
    
    
    
    return 0;
}
