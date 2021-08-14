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

enum SBCstate { boot, preflight, takeoff, shutdown } ; //SBC states

bool check_connection(); //declare USB connection check

//functions which execute child python processes
int check_BME280();
int take_image();
void log_status(std::string message, bool wtime);

int main(void)
{
    
    time_t bootTime = time(NULL);// stores epoch time;
    time_t currentTime;
    float temperatures[5]; //readout from ADC
    bool adcChannels[5] = { 1 };

    //Generate Instrument Class Objects
    Accelerometer* accel;
    ADC* adc;
    IRCSP ircsp;
    
    accel = new Accelerometer();
    adc = new ADC(accel->twifd);
   
    //make header for telemetry file
    std::fstream telemetry;
    telemetry.open(ircsp.telemetryPath,std::fstream::app);
    telemetry << "time"<<",";
    telemetry << "acceleration"<<",";
    telemetry << "t_sbc"<<",";
    telemetry << "t_ircsp"<<",";
    telemetry << "humidity"<<",";
    telemetry << "pressure"<<",";
    telemetry << "voltage"<<",";
    telemetry << "cam1_t"<<",";
    telemetry << "cam2_t";
    telemetry <<"\n";
    telemetry.close();
    
    //Status trackers for child processes
    pid_t childPid, wpid;
    SBCstate sbcState = boot;
    int status = 0;
    
    //declare start of loop
    log_status(" Main Function Initiated ", 1);

    //begin time to save telemery
    time_t tStart;
    tStart = time(NULL);

    //set loop in automata IF connected to Boson dev ports
    bool connected = 1 ;
    
    //BEGIN FINITE STATE MACHIENE
    while(connected){
        //take telemetry as dictated by the ircsp.sampling
        long double timeSpent = ( time(NULL) - tStart ) ;
        if(timeSpent > ircsp.sampling){
            
            //take telemetry measrements
            std::cout<< "telemetry check \n";
            currentTime = time(NULL);
            check_BME280(); //ping BMR280 sensor
            ircsp.check_telemetry(bootTime); //set class telemetry objects
            
            //Read in data from i2c and ADC channels
            Accelerometer::accelerometer_read(accel->twifd, &settings[0], 0x15, 4);
            accel->getAcceleration();
            adc->getVoltage(temperatures);
            ircsp.acceleration = accel->gValues[2];
            ircsp.voltage = temperatures[0];
            
            //write to telemetry.csv
            telemetry.open(ircsp.telemetryPath, std::fstream::app);
            telemetry << currentTime <<",";
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
            
            //print telemetry info
            std::cout << "acceleration = "<<ircsp.acceleration << "\n";
            std::cout << "humidity = "<< ircsp.humidity<<  " % \n";
            std::cout << "pressure = "<< ircsp.pressure<<  " hPa \n";
            std::cout << "housing temp = "<< ircsp.t_ircsp<<  " C \n";
            std::cout << "camera 1 is " << ircsp.cam1_t << " C \n";
            std::cout << "camera 2 is " <<ircsp.cam2_t << " C \n ";   
            
            //reset telemetry timer
            tStart = time(NULL);
        }

        switch (sbcState) //state handler
        {
            case boot:
                //print status to cout and log
                std::cout << " System Booting "  ;
                log_status( " System Booting ", 1 ) ;
                
                //switch conditions
                if (bootTime != .1){
                    //wait until booted
                    sleep(5);
                }
                    
                if(ircsp.cam1_t < 25 || ircsp.cam2_t < 25){   //assume instrument is at altitude is cameras are cold
                    sbcState = takeoff;
                    currentTime = time(NULL);
                    log_status(" Entering TakeOff " , 1);
                    log_status(" Acceleration = " + std::to_string( ircsp.acceleration ) + "G \n", 0);
                    log_status(" Preflight time = " + std::to_string(bootTime - currentTime ) + "s \n", 0);
                }
                
                else{
                    sbcState = preflight;
                    std::cout <<"preflight \n";
                    log_status( " Entering Preflight " , 1);
                }
                break;
                
            case preflight:
                //take telemetry measrements
                check_BME280();
                ircsp.check_telemetry(bootTime);
                Accelerometer::accelerometer_read(accel->twifd, &settings[0], 0x15, 4);
                accel->getAcceleration();
                ircsp.acceleration = accel->gValues[2];
                currentTime = time(NULL);
                    
                //SWITCH CONDITION
                if (currentTime - bootTime > ircsp.PREFLIGHT_TIME || ircsp.acceleration > ircsp.TAKEOFF_ACCEL ){
                    
                    sbcState = takeoff;
                    std::cout << "take-off \n";
                    log_status(" Entering TakeOff " , 1);
                    log_status(" Acceleration = " + std::to_string( ircsp.acceleration ) + "G", 0);
                    log_status(" Preflight time = " + std::to_string(currentTime -bootTime ) + "s", 0);
                }
            break;

                    
            case takeoff:
                //take telemetry measrements
                check_BME280();
                ircsp.check_telemetry(bootTime);
                Accelerometer::accelerometer_read(accel->twifd, &settings[0], 0x15, 4);
                accel->getAcceleration();
                ircsp.acceleration = accel->gValues[2];
                currentTime = time(NULL);
                
                take_image();
                
                if (ircsp.dataspace > ircsp.MAX_DATA){
                    sbcState = shutdown;
                    log_status(" Data Max Reached, Shutting Down " , 1 );
                    log_status(" Acceleration = " + std::to_string( ircsp.acceleration ) + "G", 0);
                    log_status(" flight time = " + std::to_string(currentTime -bootTime) + "s", 0);
                }
                
                break;

                                    
            case shutdown:
                sleep(10);
                //system("ts7800ctl -s 3600"); // put SBC in sleep mode
                break;
                    
        }
        while ((wpid = wait(&status)) > 0); //wait for child to finish
        sleep(ircsp.wait_time);
       
    }
    
    return 0;
}


int check_BME280(){
    int status;
    pid_t childPid;
    if((childPid = fork()) == 0 ){
        execlp("python3","python3","/mnt/sdcard/image_data/read_therm.py","read_therm.py");
        perror("error");
        log_status("BME check error" ,1);
        log_status(strerror(errno), 0);
        exit(errno);
    }
    while(wait(&status) > 0);
    return status;
}

int take_image(){
    int status;
    pid_t childPid;
    if((childPid = fork()) == 0 ){
        execlp("python3","python3","/mnt/sdcard/image_data/image_capture.py","image_capture.py");
        perror("error");
        log_status("imag. aq. error" ,1);
        log_status(strerror(errno), 0);
        exit(errno);
    }
    while(wait(&status) > 0);
    return status;
}

void log_status(std::string message, bool wtime){
    std::fstream log;
    time_t localtime = time(NULL) ;
    log.open (ircsp.logPath,std::fstream::app);
    if(wtime){
        log <<  ctime(&localtime) << message << "\n" ;
    }
    else{
        log << message << "\n" ;
    }
    log.close();
}
