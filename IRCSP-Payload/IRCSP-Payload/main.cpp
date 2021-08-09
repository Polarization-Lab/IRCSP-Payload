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
#include <linux/pci.h>
#include <unistd.h>
#include <termios.h>
#include <iostream>
#include <stdexcept>
#include<sstream>



#include "TEC.h"
#include "IRCSP.h"
#include "Accelerometer.h"
#include "NTCThermistorDecoder.h"



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
    NTCThermistorDecoder adc;
    TEC tec;
    
    //Gereate logging objects and files in append mode
    std::fstream log;
    std::fstream telemetry;
    log.open (ircsp.logPath,std::fstream::app);
    telemetry.open (ircsp.telemetryPath,std::fstream::app);
    
    //declare start of loop
    currentTime = time(NULL);
    log << " Main Function Initiated " << ctime(&currentTime)  ;
    log.close();
    telemetry.close();
    
    //Other Main funct. variables
    pid_t childPid;

    //begin time to save telemery
    time_t t;
    t = time(NULL);


    while(ircsp.time_elapsed < ircsp.MAX_TIME)
        
    {
        log.open (ircsp.logPath,std::fstream::app);
        telemetry.open (ircsp.telemetryPath,std::fstream::app);
        long double timeSpent =   ( time(NULL) - t ) ;
        
        if(timeSpent > ircsp.sampling){
            currentTime = time(NULL);
            ircsp.check_telemetry(bootTime,accelerometer,tec);
            
            
            
            telemetry << ircsp.acceleration << " ";
            telemetry << ircsp.t_sbc << " ";
            telemetry << ircsp.t_ircsp  << " ";
            telemetry << ircsp.humidity << " ";
            telemetry << ircsp.cam1_t << " ";
            telemetry << ircsp.cam2_t << " ";
            telemetry << ctime(&currentTime);
            
            t = time(NULL);
        }

        switch (sbcState) //state handler
        {
            case boot:
                currentTime = time(NULL);
                log << " System Booting "   << ctime(&currentTime) ;
                accelerometer.setMotionFreefallInterupt((float)1.4, 0b100, true);
                tec.setParams(0, 4, 4, 0);
                
                if (bootTime != .1)//boot check //do once while leaving
                {   sbcState = boot;
                    //print message to log
                    ircsp.check_telemetry(bootTime,accelerometer,tec);
                    currentTime = time(NULL);
                    
                    //toggle to next state
                    if(ircsp.cam1_t < 10 || ircsp.cam2_t < 10){//check if at altitude
                        sbcState = cruising;
                        log <<  " Cruising "  << ctime(&currentTime) ;
                    }
                    else{
                        sbcState = preflight;
                        log  << " Entering Preflight  " << ctime(&currentTime) ;
                    }
                    ircsp.toggle();
                break;
            }
            
            case preflight:
                
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                sbcState = preflight;
                
                
                //SWITCH CONDITION
                if (ircsp.time_elapsed > ircsp.PREFLIGHT_TIME || ircsp.acceleration > ircsp.TAKEOFF_ACCEL )
                {

                    sleep(ircsp.wait_time);
                    
                    sbcState = takeoff;
                    ircsp.toggle();
                    
                    currentTime = time(NULL);
                    log <<  " Entering TakeOff "   << ctime(&currentTime)  ;
                    log << ircsp.acceleration <<" " << ircsp.t_sbc <<" " << ircsp.t_ircsp<<" " << ircsp.humidity << "\n"  ;
                    tec.singleByteCommand('A');
                }
                break;

                
            case takeoff:
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                
                if((childPid = fork()) == 0) {
                execlp("/Users/kirahart/opt/anaconda3/bin/python", "python","/Users/kirahart/Documents/Github/IRSCP-Payload/IRCSP-Payload/image_capture.py",NULL);
                }
                sleep(ircsp.wait_time);
                kill(childPid, SIGKILL);
 
                sbcState = takeoff;
                //SWITCH CONDITION
                if (ircsp.acceleration < ircsp.CRUISE_ACCEL || ircsp.dataspace > ircsp.MAX_DATA)
                    
                {
                    sbcState = cruising;
                    ircsp.toggle();
                    
                    log <<  " Cruising "  << ctime(&currentTime)   ;
                    log << ircsp.acceleration <<" " << ircsp.t_sbc <<" " << ircsp.t_ircsp<<" " << ircsp.humidity<< " \n";
                }
                break;


                
            case cruising:
    
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                
                if((childPid = fork()) == 0) {
                execlp("/Users/kirahart/opt/anaconda3/bin/python", "python","/Users/kirahart/Documents/Github/IRSCP-Payload/IRCSP-Payload/image_capture.py",NULL);
                    ;
                }
                sleep(ircsp.wait_time);
                kill(childPid, SIGKILL);
                
                //SWITCH CONDITION
                if (ircsp.acceleration > ircsp.DECENT_ACCEL )
                {
                    sbcState = falling;
                    ircsp.toggle();
                    
                    log <<  " Falling "  << ctime(&currentTime)  ;
                    log << ircsp.acceleration <<" " << ircsp.t_sbc <<" " << ircsp.t_ircsp<<" " << ircsp.humidity << " \n";
                }
                if (ircsp.dataspace > ircsp.MAX_DATA)
                {
                    sbcState = shutdown;
                    ircsp.toggle();
                    
                    log << " Data Max Reached, Shutting Down "  << ctime(&currentTime)  ;
                    std::cout<< "Total Data Size = " << ircsp.GetStdoutFromCommand("du -h " + ircsp.dataPath) << "K \n";
                    log << ircsp.acceleration <<" " << ircsp.t_sbc <<" " << ircsp.t_ircsp<<" " << ircsp.humidity << " \n";
                }
                break;

                
            case falling:
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                //SWITCH CONDITION
                if (ircsp.dataspace > ircsp.MAX_DATA )
                {
                    log << ctime(&currentTime) << " Data Max Reached, Shutting Down \n"  ;
                    log << ircsp.acceleration <<" " << ircsp.t_sbc <<" " << ircsp.t_ircsp<<" " << ircsp.humidity << " \n";
                    sbcState = shutdown;
                    ircsp.toggle();
                    std::cout<< "Total Data Size = " << ircsp.GetStdoutFromCommand("du -hk " + ircsp.dataPath) << "K \n";
                }
                break;
            
            case shutdown:
                ircsp.check_telemetry(bootTime,accelerometer,tec);
                //system("ts7800ctl -s 3600"); // put SBC in sleep mode
                break;
                
        }
        log.close();
        telemetry.close();
    }
    
    
    
    
    return 0;
}
