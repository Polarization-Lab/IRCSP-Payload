#include <cstdio>
#include <cmath>
#include "TECTTL.h"
#include "Accelerometer.h"
#include "NTCThermistorDecoder.h"
#include "Balloon.h"
#include <time.h>
#include <sys/mman.h>
#include <linux/pci.h>
#include <unistd.h>
#include <termios.h>

#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>

#define MIN_ASCENT_RATE 60/60 //60 m/60 sec == 200ft / 60sec
#define MAX_PREFLIGHT_TIME 60 //seconds
//#define DEBUG

#ifdef DEBUG
#include <pwd.h>
#endif // DEBUG


typedef enum SBCstate_enum { boot, preflight, takeoff, cruising, falling, lowTemp } SBCstate; //SBC states

static __off_t get_fpga_phy(void);

int main()
{   
    time_t bootTime = time(NULL), currentTime, lastAccelCheck = bootTime; // stores epoch time; 
    volatile SBCstate lastState, sbcState = boot;
    
    Accelerometer* accel;
    float temperatures[5];
    NTCThermistorDecoder* adc;
    bool adcChannels[5] = { 1 };
    const float NTCparam[4][5] = { {4.46}, { 10700 }, { 25 + 273}, { 10000 } }; //source voltage, resistors, reference Temp, thermistor reference temperature, thermistor sensitivty
    const float NKA103C1R1CCoef[5][4] = { { 3.3539438E-03, 2.5646095E-04, 2.5158166E-6, 1.0503069E-07} }; 
    TECTTL* tec;
    Balloon* balloon;
    
    bool motionInterupt;
    int childPid, childStatus;
    char testChar[256] = "empty", testMsg[256], testChar2[256];
    
    uint8_t settings[4];

    int devmem = open("/dev/mem", O_RDWR | O_SYNC);
    if (devmem < 0) {
        fprintf(stderr, "Error:  Can't open /dev/mem\n");
        return 1;
    }
    __off_t syscon_phy;
    if ((syscon_phy = get_fpga_phy()) == 0) {
        fprintf(stderr, "Warning:  Did not discover FPGA base from PCI probe\n");
        syscon_phy = (__off_t)0xFC081000;
    }

    volatile unsigned int* syscon = (unsigned int*)mmap(NULL, getpagesize(), PROT_READ | PROT_WRITE, MAP_SHARED, devmem, syscon_phy); //shares the FPGA syscondition address for R/W // any address, page size, permisions, properties, file descriptor, offset to FPGA
    int n;
#ifdef DEBUG

    struct passwd* pw = getpwuid(getuid());

    const char* homedir = pw->pw_dir;
#endif // DEBUG
    //int fdttyS8 = open("/dev/ttyS8", O_RDWR | O_SYNC);
    ////unsigned char* conttyS8 = (unsigned char*)mmap(NULL, getpagesize(), PROT_READ | PROT_WRITE, MAP_SHARED, fdttyS8, 0);

    //int fdttyS1 = open("/dev/ttyS1", O_RDWR | O_SYNC);
    ////unsigned char* conttyS1 = (unsigned char*)mmap(NULL, getpagesize(), PROT_READ | PROT_WRITE, MAP_SHARED, fdttyS1, 0);

    accel = new Accelerometer();
    adc = new NTCThermistorDecoder(accel->twifd, adcChannels, NTCparam[0], NTCparam[1], NTCparam[2], NTCparam[3], NKA103C1R1CCoef);
    balloon = new Balloon();
    tec = new TECTTL();
    sleep(1);

    //int fdttyS9 = open("/dev/ttyS9", O_RDWR | O_NONBLOCK ); //com3 rs232
    //struct termios ttyS9;
    //tcgetattr(tec->getfd(), &ttyS9);
    //tcsetattr(fdttyS9, TCSANOW, &ttyS9);


    #ifdef DEBUG
    fprintf(stderr, "new test\n");
    #endif
    
    while (1) {//automata loop

        switch (sbcState) //state handler
        {
        
        case boot:
        #ifdef DEBUGSTATE
            fprintf(stderr, "boot\n");
        #endif // DEBUG
            
        #ifdef DEBUG
            Accelerometer::accelerometer_read(accel->twifd, &settings[0], 0x15, 4);
        #endif // DEBUG

            /*n = read(fdttyS9, testChar, 100);
            n = write(fdttyS9, testChar, n);*/
            

            if (true && bootTime != .1)//boot check //do once while leaving
            {
                sbcState = preflight;
                accel->setMotionFreefallInterupt((float)1.4, 0b100, true);
                tec->setParams(0, 4, 4, 0);
                sleep(1);
            }
            break;
        
        case preflight:

            #ifdef DEBUGSTATE
            fprintf(stderr, "preflight\n");
            #endif // DEBUG
            if ((n= time(&currentTime)-lastAccelCheck) >= 60)//time since last check > 1min
            {
                lastAccelCheck = currentTime;
                motionInterupt = accel->checkMotionInteruptFlag(NULL);
                #ifdef DEBUG
                accel->getAcceleration();
                #endif // DEBUG
            }
            adc->getTemp(temperatures);
            balloon->readBuf();

           /* tec->clearBuffer();
            tec->sendParams();
            tec->getSingleReadout(testChar);
            fprintf(stderr, "I am: %s", testChar);
            tec->getSingleReadout(testChar2);
            adc->getTemp(temperatures);
            fprintf(stderr, "Hot Side: %+.2f, Cold Side: %+.2f", temperatures[0] - 273.15, tec->Tr);
            */
            
            //syscon[(0xc / 4)] &= ~(1 << 20); //turn red led off
            //syscon[(0xc / 4)] |= (1 << 20); //turn red led on

            //strcpy(testMsg,"$GPGGA,233656.000,3146.75029,N,09542.98104,W,1,12,0.8,138.42,M,-24.0,M,,*52\r\n");
            //write(fdttyS7, testMsg, strlen(testMsg)); //note doesnt send '\0'
            //usleep(100);
            //balloon->readBuf();
            //strcpy(testMsg, "$GPGGA,233707.000,3146.75029,N,09542.98104,W,1,13,0.8,238.42,M,-24.0,M,,*56\r\n");
            //write(fdttyS7, testMsg, strlen(testMsg));
            //usleep(100);

            if (true || balloon->ascentRate > MIN_ASCENT_RATE || motionInterupt || time(&currentTime) - bootTime > MAX_PREFLIGHT_TIME) //do once while leaving
            {
                sbcState = takeoff;
                motionInterupt = false;
                tec->singleByteCommand('A');
                sleep(1);
                if ((childPid = fork()) == 0)
                {
                    system("ts7800ctl -t");
                    execlp("ts7800ctl", "ts7800ctl", "-t", NULL);
                }
                waitpid(childPid, &childStatus, 0);
            }
            break;

        case takeoff:
            #ifdef DEBUGSTATE
            fprintf(stderr, "takeoff\n");
            #endif // DEBUG
            balloon->readBuf();
            adc->getTemp(temperatures);
            //get camera temperature

            if (balloon->ascentRate < MIN_ASCENT_RATE) //do once while leaving
            {
                sbcState = cruising;
                accel->setMotionFreefallInterupt(.1, 0b100, false);
                tec->setParams(-20, 4, 4, 0);
                sleep(1);
            }

            if (temperatures[0] <= -40) { //check camera temperatures
                lastState = sbcState;
                tec->setParams(-20, 20, 0, 0);
                //user signal turn off cameras
                sleep(1);
            }
            break;

        case cruising:
            balloon->readBuf();
            adc->getTemp(temperatures);
            //get camera temp

            #ifdef DEBUGSTATE
            fprintf(stderr, "cruising\n");
            #endif // DEBUG
            if ((n = time(&currentTime) - lastAccelCheck) >= 60) {
                lastAccelCheck = currentTime;
                motionInterupt = accel->checkMotionInteruptFlag(NULL);
            }
            
            if (motionInterupt) {
                kill(childPid, SIGTERM);
                sbcState = falling;
            }

            if (temperatures[0] <= -40) {
                lastState = sbcState;
                tec->setParams(-20, 20, 0, 0);
                //user signal turn off cameras
                sleep(1);
            }
            break;

        case falling:
            #ifdef DEBUGSTATE
            fprintf(stderr, "falling\n");
            #endif // DEBUG
            delete balloon;
            delete tec;
            delete accel;
            delete adc;
            system("ts7800ctl -s 3600");
            break;

        case lowTemp:
            adc->getTemp(temperatures);
            if (temperatures[0] > -40) {
                sbcState = lastState;
                tec->setParams(-20, 20, 0, 0);
                //user signal turn on camreas
                sleep(1);
            }
        }
    }
}

static __off_t get_fpga_phy(void)
{
    static __off_t fpga = 0;

    if (fpga == 0) {
        unsigned int config[PCI_STD_HEADER_SIZEOF];
        FILE* f = fopen("/sys/bus/pci/devices/0000:03:00.0/config", "r");

        if (fread(config, 1, sizeof(config), f) > 0) {
            if (config[PCI_BASE_ADDRESS_2 / 4])
                fpga = config[PCI_BASE_ADDRESS_2 / 4];
        }
        else
            fprintf(stderr, "Can't read from the config!\n");
        fclose(f);
    }

    return fpga;
}