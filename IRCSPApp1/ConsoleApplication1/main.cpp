#include <cstdio>
#include <cmath>
#include "TECTTL.h"
#include "Accelerometer.h"
#include "ADC.h"
#include "Balloon.h"
#include <time.h>
#include <sys/mman.h>
#include <linux/pci.h>
#include <unistd.h>
#include <termios.h>
#define MIN_ASCENT_RATE 60/60 //60 m/60 sec == 200ft / 60sec
#define DEBUG

#ifdef DEBUG
#include <pwd.h>
#endif // DEBUG


typedef enum SBCstate_enum { boot, preflight, takeoff, cruising, falling } SBCstate; //SBC states

static __off_t get_fpga_phy(void);

int main()
{   
    time_t bootTime = time(NULL), currentTime; // stores epoch time; 
    volatile SBCstate sbcState = boot;
    Accelerometer* accel;
    ADC* adc;
    TECTTL* tec;
    Balloon* balloon;
    bool motionInterupt;
    char testChar[256] = "empty", testMsg[256];
    
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

    unsigned int* syscon = (unsigned int*)mmap(NULL, getpagesize(), PROT_READ | PROT_WRITE, MAP_SHARED, devmem, syscon_phy); //shares the FPGA syscondition address for R/W // any address, page size, permisions, properties, file descriptor, offset to FPGA

#ifdef DEBUG

    struct passwd* pw = getpwuid(getuid());

    const char* homedir = pw->pw_dir;

    //int fdttyS8 = open("/dev/ttyS8", O_RDWR | O_SYNC);
    ////unsigned char* conttyS8 = (unsigned char*)mmap(NULL, getpagesize(), PROT_READ | PROT_WRITE, MAP_SHARED, fdttyS8, 0);

    //int fdttyS1 = open("/dev/ttyS1", O_RDWR | O_SYNC);
    ////unsigned char* conttyS1 = (unsigned char*)mmap(NULL, getpagesize(), PROT_READ | PROT_WRITE, MAP_SHARED, fdttyS1, 0);

    int fdttyS7 = open("/dev/ttyS7", O_RDWR | O_NONBLOCK | O_NOCTTY); //com3 rs232
    struct termios ttyS7;
    tcgetattr(fdttyS7, &ttyS7);
    cfmakeraw(&ttyS7);
    ttyS7.c_cflag &= ~(PARENB | CSTOPB);
    ttyS7.c_lflag |= ICANON;
    tcsetattr(fdttyS7, TCSANOW, &ttyS7);

    int fdttyS9 = open("/dev/ttyS9", O_RDWR | O_NONBLOCK | O_NOCTTY); //extra lcd ttl
    struct termios ttyS9;
    tcgetattr(fdttyS9, &ttyS9);
    cfmakeraw(&ttyS9);
    ttyS9.c_cflag &= ~(PARENB | CSTOPB);
    ttyS9.c_lflag &= ~ICANON;
    tcsetattr(fdttyS9, TCSANOW, &ttyS9);

    fprintf(stderr, "new test\n");
#endif // DEBUG

    int n = 10;
    
    while (1) {//automata loop
        switch (sbcState) //state handler
        {
        case boot:
            accel = new Accelerometer();
            adc = new ADC(accel->twifd);
            balloon = new Balloon();
            tec = new TECTTL();

            usleep(100); //sleep to let messages pass 
            n = read(fdttyS9, testChar,25);
            n = write(fdttyS9, testChar, n);
            usleep(100);
            tec->getPrintOut(testChar);

            accel->setMotionFreefallInterupt((float)1.25,0b100,true);
#ifdef DEBUG
            Accelerometer::accelerometer_read(accel->twifd, &settings[0], 0x15, 4);
#endif // DEBUG

            accel->getAcceleration();

            tec->setParams(30, 1, 1, 1);
            usleep(100);
            n = read(fdttyS9, testChar, 100);
            n = write(fdttyS9, testChar, n);
            usleep(100);
            tec->getPrintOut(testChar);

            adc->ADC_init();
            adc->getADC();

            if (true && bootTime != .1)//boot check
                sbcState = preflight;
            break;
        case preflight:
            if (true)//time since last check > 1min
            {
                motionInterupt = accel->checkMotionInteruptFlag(NULL);
#ifdef DEBUG
                accel->getAcceleration();
#endif // DEBUG
            }

            syscon[(0xc / 4)] &= ~(1 << 20); //turn red led off
            syscon[(0xc / 4)] |= (1 << 20); //turn red led on

            strcpy(testMsg,"$GPGGA,233656.000,3146.75029,N,09542.98104,W,1,12,0.8,138.42,M,-24.0,M,,*52\r\n");
            write(fdttyS7, testMsg, strlen(testMsg)); //note doesnt send '\0'
            usleep(100);
            balloon->readBuf();
            strcpy(testMsg, "$GPGGA,233707.000,3146.75029,N,09542.98104,W,1,13,0.8,238.42,M,-24.0,M,,*56\r\n");
            write(fdttyS7, testMsg, strlen(testMsg));
            usleep(100);
            balloon->readBuf();

            tec->sendParams();
            usleep(100);
            n = read(fdttyS9, testChar, 100);
            n = write(fdttyS9, testChar, n);
            usleep(100);
            tec->getPrintOut(testChar);


            if (balloon->ascentRate > MIN_ASCENT_RATE || motionInterupt || time(&currentTime) - bootTime > 4 * 3600)
            {
                sbcState = takeoff;
                motionInterupt = false;
            }
            break;
        case takeoff:

            if (balloon->ascentRate < MIN_ASCENT_RATE)
            {
                sbcState = cruising;
                accel->setMotionFreefallInterupt(.1, 0b001, false);
            }
            break;
        case cruising:
            if (true)
                motionInterupt = accel->checkMotionInteruptFlag(NULL);
            if (motionInterupt)
                sbcState = falling;
            break;
        case falling:
            break;
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