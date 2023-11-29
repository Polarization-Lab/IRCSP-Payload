#include <cstdio>
#include <cmath>
#include <time.h>
#include <sys/mman.h>
#include <linux/pci.h>
#include <sys/reboot.h>
#include <unistd.h>
#include <termios.h>
#include <sys/wait.h>
#include <signal.h>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <sstream>

//to check dev ports
#include <sys/types.h>
#include <sys/stat.h>

//instrument control headers
#include "ADC.h"
#include "Accelerometer.h"
#include "IRCSP.h"
#include "IRCSP.cpp"


enum SBCstate { boot, preflight, takeoff, flight, shutdown } ; //SBC states
//include another ascension state if time permits

//functions to check if cameras and BME280 have disconnected
bool port_exists(const char* dev); //checks if dev port exists
bool check_connection(); //check for bool connection

//functions which execute child python processes
int check_BME280();
int check_BME280slow();
int take_image();
int find_file();
int take_dummy_image();
int TEC_set_roomtemp();
int TEC_set_flight_temp();
void log_status(std::string message, bool wtime);
bool time_up(float hours);

int main(void){
    
    //check time in flight
    bool inpreflight = 1;
    float preflight_time = 3; //hours in preflight state
    int count; 
    

    time_t bootTime = time(NULL);// stores epoch time;
    time_t currentTime;
    float temperatures[5]; //readout from ADC
    bool adcChannels[5] = { 1 };
    uint8_t settings[4];

    //Generate Instrument Class Objects
    Accelerometer* accel;
    ADC* adc;
    IRCSP ircsp;
    
    accel = new Accelerometer();
    adc = new ADC(accel->twifd);
   
    //make header for telemetry file
    std::fstream telemetry;
    telemetry.open(ircsp.telemetryPath,std::fstream::app);
    telemetry << "time_elapsed"<<",";
    telemetry << "acceleration"<<",";
    telemetry << "t_sbc"<<",";
    telemetry << "t_amb"<<",";
    telemetry << "amb_humidity"<<",";
    telemetry << "amb_pressure"<<",";
    telemetry << "t_elec"<<",";
    telemetry << "elec_humidity"<<",";
    telemetry << "elec_pressure"<<",";
    telemetry << "t_ircsp"<<",";
    telemetry << "ircsp_humidity"<<",";
    telemetry << "ircsp_pressure"<<",";
    telemetry << "voltage"<<",";
    telemetry << "t_cam1"<<",";
    telemetry << "t_cam2"<<",";
    telemetry << "thermVal"<<",";
    telemetry << "therm_temp"<<",";
    telemetry << "contextVal"<<",";
    telemetry << "context_temp"<<",";
    telemetry << "lensVal"<<",";
    telemetry << "lens_temp"<<",";
    telemetry << "heat_V" <<",";
    telemetry << "heat_temp" << ",";
    telemetry << "t_cam3";
    telemetry <<"\n";
    telemetry.close();
    
    //Status trackers for child processes
    pid_t wpid;
    SBCstate sbcState = boot;
    int status = 0;
    
    //declare start of loop
    log_status(" Main Function Initiated ", 1);

    //begin time to save telemery
    time_t tStart;
    tStart = time(NULL);

    //set loop in automata IF connected to Boson dev ports
    bool connected = 1 ;
    
    //BEGIN FINITE STATE MACHINE
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
            telemetry << ircsp.t_sbc<<",";
            telemetry << ircsp.t_amb <<",";
            telemetry << ircsp.amb_humidity <<",";
            telemetry << ircsp.amb_pressure <<",";
            telemetry << ircsp.t_elec <<",";
            telemetry << ircsp.elec_humidity <<",";
            telemetry << ircsp.elec_pressure <<",";
            telemetry << ircsp.t_ircsp <<",";
            telemetry << ircsp.ircsp_humidity <<",";
            telemetry << ircsp.ircsp_pressure <<",";
            telemetry << ircsp.voltage  <<",";
            telemetry << ircsp.t_cam1  << ",";
            telemetry << ircsp.t_cam2  << ",";
            telemetry << ircsp.thermVal  << ",";
            telemetry << ircsp.contextVal << ",";
            telemetry << ircsp.lensVal << ",";
            telemetry << ircsp.therm_temp << ",";
            telemetry << ircsp.context_temp << ",";
	    telemetry << ircsp.lens_temp << ",";
	    telemetry << ircsp.heat_temp << ",";
            telemetry << ircsp.heat_V << ",";
            telemetry << ircsp.t_cam3;
            telemetry <<"\n";
            telemetry.close();
            
            //print telemetry info
            std::cout << "acceleration = "<<ircsp.acceleration << "\n";
            std::cout << "ambient humidity = "<< ircsp.amb_humidity<<  " % \n";
            std::cout << "ambient pressure = "<< ircsp.amb_pressure<<  " mbar \n";
            std::cout << "ambient temp = "<< ircsp.t_amb<<  " C \n";
            std::cout << "electronics humidity = "<< ircsp.elec_humidity<<  " % \n";
            std::cout << "electronics pressure = "<< ircsp.elec_pressure<<  " mbar \n";
            std::cout << "electronics temp = "<< ircsp.t_elec<<  " C \n";
            std::cout << "instrument housing humidity = "<< ircsp.ircsp_humidity<<  " % \n";
            std::cout << "instrument housing pressure = "<< ircsp.ircsp_pressure<<  " mbar \n";
            std::cout << "thermistor temp = " << ircsp.therm_temp << "C \n";
            std::cout << "instrument housing temp = "<< ircsp.t_ircsp<<  " C \n";
            std::cout << "camera 1 is " << ircsp.t_cam1 << " C \n";
            std::cout << "camera 2 is " <<ircsp.t_cam2 << " C \n ";
            std::cout << "context camera is " <<ircsp.t_cam3 << " C \n ";
            std::cout << "context camera thermistor is " <<ircsp.context_temp << " C \n ";
            std::cout << "housing thermistor is " <<ircsp.therm_temp << " C \n ";
            std::cout << "housing thermistor analog value is " <<ircsp.thermVal << " C \n ";
            std::cout << "lens analog value is " <<ircsp.lensVal << " C \n ";
	    std::cout << "lens temp is" <<ircsp.lens_temp << " C \n";
	    std::cout << "heat sink is" << ircsp.heat_temp << " C \n";
	    std::cout << "heat sink value" << ircsp.heat_V << " C \n";
            std::cout << "context camera analog value is " <<ircsp.contextVal << " C \n ";
            
            //reset telemetry timer
            tStart = time(NULL);
        }

        switch(sbcState){
            case boot:
                //print status to cout and log
	
		
		// take_dummy_image();
		
		TEC_set_roomtemp();

    		std::cout << " System Booting \n"  ;
                log_status( " System Booting ", 1 ) ;
                sleep(5);
                sbcState = preflight;
                std::cout <<"Entering Preflight \n";
                log_status( " Entering Preflight " , 1);	
   
                break;
                
            case preflight:

               // TEC_set_roomtemp();
                check_BME280();
                ircsp.check_telemetry(bootTime);
                Accelerometer::accelerometer_read(accel->twifd, &settings[0], 0x15, 4);
                accel->getAcceleration();
                ircsp.acceleration = accel->gValues[2];
                currentTime = time(NULL);
                inpreflight = time_up(preflight_time);
               
	//	if (ircsp.elec_pressure < 750){
			
	//	    sbcState = flight;
	//	    std::cout << "Entering Flight \n";
	//	    log_status(" Entering Flight " , 1);
          //          log_status(" Preflight time = " + std::to_string(currentTime-bootTime ) + "s", 0);
	    //    }		    
    
                //SWITCH CONDITION
                if (ircsp.amb_pressure < 750){
                   
                    sbcState = flight;
                    std::cout << "Entering Flight \n";
                    log_status(" Entering Flight " , 1);
                    log_status(" Preflight time = " + std::to_string(currentTime -bootTime ) + "s", 0);
                }
           
	        if (!inpreflight){
		    sbcState = takeoff;
		    std::cout << "Entering Takeoff \n";
		    log_status("Entering Takeoff " , 1);
		    log_status("Preflight  time = " + std::to_string(currentTime-bootTime ) + "s", 0);
	        }
	        break;

            case takeoff:
                
                
		//TEC_set_roomtemp();
                check_BME280();
                ircsp.check_telemetry(bootTime);
                currentTime = time(NULL);
                
		take_image();
		 

                if (ircsp.amb_pressure < 750){
                    
                    sbcState = flight;
                    std::cout << "Entering Flight \n";
                    log_status(" Entering Flight " , 1);
                    log_status(" Preflight time = " + std::to_string(currentTime -bootTime ) + "s", 0);
                }
                
                if (ircsp.dataspace > ircsp.MAX_DATA){
                    sbcState = shutdown;
                    log_status(" Data Max Reached, Shutting Down " , 1 );
                    log_status(" Acceleration = " + std::to_string( ircsp.acceleration ) + "G", 0);
                    log_status(" flight time = " + std::to_string(currentTime -bootTime) + "s", 0);
                }
                break;

                    
            case flight:
                
                //TEC_set_flight_temp();
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
                sleep(100);
                break;
                    
        }
        //wait for child to finish
        while ((wpid = wait(&status)) > 0);
        
        //check that ACM communication is live, will exit while loop if not
        connected = check_connection();
        //connected = 1;
	sleep(ircsp.wait_time);
       
    }
    //if while loop is exited, reboot sbc
    log_status("lost port connection(s), rebooting", 1);
    sleep(5);
    
    sync();
    reboot(RB_AUTOBOOT);
    
    return 0;
}

int check_BME280(){
    int status;
    pid_t childPid;
    if((childPid = fork()) == 0 ){
        execlp("python3","python3","/mnt/sdcard/image_data/readsensors.py","readsensors.py",NULL);
        perror("error");
        log_status("bme280(s) error" ,1);
        log_status(strerror(errno), 0);
        exit(errno);
    }
    while(wait(&status) > 0);
    return status;
}

int check_BME280slow(){
    int status;
    pid_t childPid;
    if((childPid = fork()) == 0 ){
	execlp("python3","python3","/mnt/sdcard/image_data/readsensorsslow.py","readsensors.py",NULL);
	perror("error");
	log_status("bme280 slow error",1);
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
        execlp("python3","python3","/mnt/sdcard/image_data/image_capture.py","image_capture.py", NULL);
        perror("error");
	log_status("imag. aq. error" ,1);
        log_status(strerror(errno), 0);
        exit(errno);
    }
    while(wait(&status) > 0);
    return status;
}

int take_dummy_image(){
	int status;
	pid_t childPid;
	if((childPid = fork()) == 0 ){
	    execlp("python3","python3","/mnt/sdcard/image_data/image_start.py","image_start.py",NULL);
	    perror("error");
	    log_status("imag. aq. error",1);
	    log_status(strerror(errno), 0);
	    exit(errno);
    }
    while(wait(&status) > 0);
    return status;
}


int find_file(){
    int status;
    pid_t childPid;
    if((childPid = fork()) == 0){
	execlp("python3","python3","/mnt/sdcard/image_data/find_file.py","find_file.py",NULL);
	perror("error");
	log_status("find file error",1);
	log_status(strerror(errno),0);
	exit(errno);
    }
    while(wait(&status) > 0);
    return status;
}


int TEC_set_flight_temp(){
    int status;
    pid_t childPid;
    if((childPid = fork()) == 0 ){
        execlp("python3","python3","/mnt/sdcard/image_data/TEC_set_flight_temp.py","TEC_set_flight_temp.py",NULL);
        perror("error");
        log_status("PID error" ,1);
        log_status(strerror(errno), 0);
        exit(errno);
    }
    while(wait(&status) > 0);
    return status;
}

int TEC_set_roomtemp(){
    int status;
    pid_t childPid;
    if((childPid = fork()) == 0 ){
        execlp("python3","python3","/mnt/sdcard/image_data/TEC_set_roomtemp.py","TEC_set_roomtemp.py",NULL);
        perror("error");
        log_status("error changing TEC temp to room temperature" ,1);
        log_status(strerror(errno), 0);
        exit(errno);
    }
    while(wait(&status) > 0);
    return status;
}

void log_status(std::string message, bool wtime){
    std::fstream log;
    time_t localtime = time(NULL) ;
    log.open ("/mnt/sdcard/image_data/log.txt",std::fstream::app);
    if(wtime){
        log <<  ctime(&localtime) << message << "\n" ;
    }
    else{
        log << message << "\n" ;
    }
    log.close();
}

bool port_exists(const char* dev){ //declare USB connection check
    struct stat sb;
    return (stat(dev, &sb) == 0); // true if open, false otherwise
}

bool check_connection(){
    //define device ports that should be checked
    // three cameras and arduino 
    const char* ACM0 = "/dev/ttyACM0" ;
    const char* ACM1 = "/dev/ttyACM1" ;
    const char* ACM2 = "/dev/ttyACM2" ;
    const char* ACM3 = "/dev/ttyACM3" ;

    
    //check for existence
    bool acm0 = port_exists(ACM0);
    bool acm1 = port_exists(ACM1);
    bool acm2 = port_exists(ACM2);
    bool acm3 = port_exists(ACM3);

    
    bool existence = 1;
    
    if(acm0 && acm1 && acm2 && acm3){
        existence = 1;
    }
    if(!acm0 || !acm3 || !acm2){
        std::cout<< "camera(s) lost connection \n";
        existence = 0;
    }
    if(!acm1){
        std::cout<< "BME280 lost connection \n" ;
        existence = 0;
    }

    return existence;
}

bool time_up(float hours){ //returns true if still in preflight
    int rows=0;
    std::ifstream file("/mnt/sdcard/image_data/telemetry.csv");
    std::string line;
    while (getline(file, line))
    rows++;
    std::cout << "total rows = "<< rows << "\n";
    
  int max_rows = 10; //fix this
        //choose time for how long to be in preflight before just going into flight
    
    
    if(rows < max_rows){
        return 1 ;
    }
    else{
        return 0;
    }
}
