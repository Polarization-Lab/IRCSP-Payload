#include <cstdio>
#include <cmath>
#include "ADC.h"
#include "Accelerometer.h"
#include <time.h>
#include <sys/mman.h>
#include <linux/pci.h>
#include <unistd.h>
#include <termios.h>
#include "IRCSP.h"

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

enum SBCstate { boot, preflight, takeoff, cruising,  shutdown } ; //SBC states

int main(void)
{
    
    time_t bootTime = time(NULL);// stores epoch time;
    time_t currentTime;
    float temperatures[5]; //readout from ADC
    bool adcChannels[5] = { 1 };
    bool motionInterupt;
    uint8_t settings[4];

    //Generate Instrument Class Objects
    Accelerometer* accel;
    ADC* adc;
    IRCSP ircsp;
    
    accel = new Accelerometer();
    adc = new ADC(accel->twifd);
   
  
    
    //Gereate logging objects and files in append mode
    std::fstream log;
    std::fstream telemetry;
    log.open(ircsp.logPath,std::fstream::app);
    telemetry.open(ircsp.telemetryPath,std::fstream::app);
    
    //make header for telemetry file
    telemetry << "time_elapsed"<<",";
    telemetry << "acceleration"<<",";
    telemetry << "t_sbc"<<",";
    telemetry << "t_ircsp"<<",";
    telemetry << "humidity"<<",";
    telemetry << "pressure"<<",";
    telemetry << "voltage"<<",";
    telemetry << "cam1_t"<<",";
    telemetry << "cam2_t";
    telemetry <<"\n";
    
    
    //declare start of loop
    currentTime = time(NULL);
    log << " Main Function Initiated " << ctime(&currentTime)  ;
    
    log.close();
    telemetry.close();
    
    //Other Main funct. variables
    pid_t childPid, wpid;
    SBCstate sbcState = boot;
    int status = 0;

    //begin time to save telemery
    time_t t;
    t = time(NULL);


    while(ircsp.time_elapsed < ircsp.MAX_TIME)
    {
        long double timeSpent =   ( time(NULL) - t ) ;
        if(timeSpent > ircsp.sampling)
        {
            //take telemetry measrements
            if((childPid = fork())== 0)
            {
                execlp("python3","python3","/mnt/sdcard/image_data/read_therm.py","read_therm.py");
                exit(EXIT_SUCCESS);
            }
            while ((wpid = wait(&status)) > 0); //wait for child to finish
                
            ircsp.check_telemetry(bootTime);
            
            Accelerometer::accelerometer_read(accel->twifd, &settings[0], 0x15, 4);
            accel->getAcceleration();
            adc->getVoltage(temperatures);
            ircsp.acceleration = accel->gValues[2];
            ircsp.voltage = temperatures[0];
                
            std::cout<< "telemetry check \n";
            currentTime = time(NULL);

            telemetry.open(ircsp.telemetryPath, std::fstream::app);
            telemetry << ircsp.time_elapsed<<",";
            telemetry << ircsp.acceleration<<",";
            telemetry << ircsp.t_sbc   <<",";
            telemetry << ircsp.t_ircsp <<",";
            telemetry << ircsp.humidity <<",";
            telemetry << ircsp.pressure <<",";
            telemetry << ircsp.voltage  <<",";
            telemetry << ircsp.cam1_t  << ",";
            telemetry << ircsp.cam2_t;
            telemetry <<"\n";
            telemetry.close();
                
            std::cout << "acceleration = "<<ircsp.acceleration << "\n";
            std::cout << "humidity = "<< ircsp.humidity<<  " % \n";
            std::cout << "pressure = "<< ircsp.pressure<<  " hPa \n";
            std::cout << "housing temp = "<< ircsp.t_ircsp<<  " C \n";
            std::cout << "camera 1 is " << ircsp.cam1_t << " C \n";
            std::cout << "camera 2 is " <<ircsp.cam2_t << " C \n ";   

            t = time(NULL);
        }

        switch (sbcState) //state handler
        {
            case boot:
                currentTime = time(NULL);
                std::cout << " System Booting "   << ctime(&currentTime) ;
                
                log.open(ircsp.logPath,std::fstream::app);
                log << " System Booting "   << ctime(&currentTime) ;
                log.close();

                if (bootTime != .1)//boot check //do once while leaving
                {
                    sbcState = boot ;

                    //take telemetry measrements
                    if((childPid = fork())== 0)
                    {
                        execlp("python3","python3","/mnt/sdcard/image_data/read_therm.py","read_therm.py");
                        exit(EXIT_SUCCESS)
                    }
                    while ((wpid = wait(&status)) > 0); //wait for child to finish
                    
                    ircsp.check_telemetry(bootTime);
                    Accelerometer::accelerometer_read(accel->twifd, &settings[0], 0x15, 4);
                    accel->getAcceleration();
                    adc->getVoltage(temperatures);
                    currentTime = time(NULL);
                    ircsp.acceleration = accel->gValues[2];
                    ircsp.voltage = temperatures[0];
                }
                    
                if(ircsp.cam1_t < 10 || ircsp.cam2_t < 10)
                {//check if at altitude
                    sbcState = cruising;
                    log.open(ircsp.logPath,std::fstream::app);
                    log <<  " Cruising "  << ctime(&currentTime) ;
                    log.close();
                }
                else
                {
                    sbcState = preflight;
                    std::cout <<"preflight \n";
                    
                    log.open(ircsp.logPath,std::fstream::app);
                    log  << " Entering Preflight  " << ctime(&currentTime) ;
                    log.close();
                }

                break;
                
            case preflight:
                //take telemetry measrements
                if((childPid= fork())== 0)
                {
                    execlp("python3","python3","/mnt/sdcard/image_data/read_therm.py","read_therm.py");
                    exit(EXIT_SUCCESS);
                }
                while ((wpid = wait(&status)) > 0); //wait for child to finish
                
                ircsp.check_telemetry(bootTime);
                Accelerometer::accelerometer_read(accel->twifd, &settings[0], 0x15, 4);
                accel->getAcceleration();
                adc->getVoltage(temperatures);
                currentTime = time(NULL);
                ircsp.acceleration = accel->gValues[2];
                ircsp.humidity = temperatures[0];
                    
                    
                //SWITCH CONDITION
                if (ircsp.time_elapsed > ircsp.PREFLIGHT_TIME || ircsp.acceleration > ircsp.TAKEOFF_ACCEL )
                {
                    std::cout << "take-off \n";
                    sleep(ircsp.wait_time);
                        
                    sbcState = takeoff;
                        
                    currentTime = time(NULL);
                    log.open(ircsp.logPath,std::fstream::app);
                    log <<  " Entering TakeOff "   << ctime(&currentTime)  ;
                    log << ircsp.acceleration <<" " << ircsp.t_sbc <<" " << ircsp.t_ircsp<<" " << ircsp.humidity << "\n"  ;
                    log.close();
		}
            break;

                    
            case takeoff:
                //take telemetry measrements
                if((childPid = fork())== 0)
                {
                    execlp("python3","python3","/mnt/sdcard/image_data/read_therm.py","read_therm.py");
                    exit(EXIT_SUCCESS);
                }
                while ((wpid = wait(&status)) > 0); //wait for child to finish
                
                ircsp.check_telemetry(bootTime);
                Accelerometer::accelerometer_read(accel->twifd, &settings[0], 0x15, 4);
                accel->getAcceleration();
                adc->getVoltage(temperatures);
                currentTime = time(NULL);
                ircsp.acceleration = accel->gValues[2];
                ircsp.humidity = temperatures[0];
                
                //std::cout << "entering image aq. state \n";
                if((childPid = fork()) == 0)
                {
                    execlp("python3","python3","/mnt/sdcard/image_data/image_capture.py","image_capture.py");
                    exit(EXIT_SUCCESS);
                }
                while ((wpid = wait(&status)) > 0); //wait for child to finish
                

                //SWITCH CONDITION
                if (ircsp.acceleration < ircsp.CRUISE_ACCEL || ircsp.dataspace > ircsp.MAX_DATA)
                {
                    std::cout<< "entering cruise state, takeoff";
                    sbcState = cruising;
                    log.open(ircsp.logPath,std::fstream::app);
                    log <<  " Cruising "  << ctime(&currentTime)   ;
                    log << ircsp.acceleration <<" " << ircsp.t_sbc <<" " << ircsp.t_ircsp<<" " << ircsp.humidity<< " \n";
                    log.close();
		}

                break;


                    
            case cruising:
                //take telemetry measrements
                if((childPid = fork())== 0)
                {
                    execlp("python3","python3","/mnt/sdcard/image_data/read_therm.py","read_therm.py");
                    exit(0);
                }
                while ((wpid = wait(&status)) > 0); //wait for child to finish
                
                ircsp.check_telemetry(bootTime);
                Accelerometer::accelerometer_read(accel->twifd, &settings[0], 0x15, 4);
                accel->getAcceleration();
                adc->getVoltage(temperatures);
                currentTime = time(NULL);
                ircsp.acceleration = accel->gValues[2];
                ircsp.humidity = temperatures[0];
                
                //std::cout << "entering image aq. state, cruising";
                if((childPid = fork()) == 0)
                {
                    execlp("python3","python3","/mnt/sdcard/image_data/image_capture.py","image_capture.py");
                    exit(EXIT_SUCCESS);
                }
                while ((wpid = wait(&status)) > 0); //wait for child to finish
                
                    
                //SWITCH CONDITION
                if (ircsp.dataspace > ircsp.MAX_DATA)
                {
                    sbcState = shutdown;
                    log.open(ircsp.logPath,std::fstream::app);
                    log << " Data Max Reached, Shutting Down "  << ctime(&currentTime)  ;
                    std::cout<< "Total Data Size = " << ircsp.GetStdoutFromCommand("du -h " + ircsp.dataPath) << "K \n";
                    log << ircsp.acceleration <<" " << ircsp.t_sbc <<" " << ircsp.t_ircsp<<" " << ircsp.humidity << " \n";
                    log.close();
                }
                
                break;

                                    
            case shutdown:
                //take telemetry measrements
                if((childPid = fork())== 0)
                {
                    execlp("python3","python3","/mnt/sdcard/image_data/read_therm.py","read_therm.py");
                    fprintf(stdout, "failed\n");
                    exit(EXIT_SUCCESS);
                }
                while ((wpid = wait(&status)) > 0); //wait for child to finish
                
                
                ircsp.check_telemetry(bootTime);
                Accelerometer::accelerometer_read(accel->twifd, &settings[0], 0x15, 4);
                accel->getAcceleration();
                adc->getVoltage(temperatures);
                currentTime = time(NULL);
                ircsp.acceleration = accel->gValues[2];
                ircsp.humidity = temperatures[0];
                    
                //system("ts7800ctl -s 3600"); // put SBC in sleep mode
                
                break;
                    
        }
        while ((wpid = wait(&status)) > 0); //wait for child to finish
        sleep(ircsp.wait_time);
       
    }
    
    return 0;
}
