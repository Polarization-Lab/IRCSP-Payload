#include <cstdio>
#include <cmath>
#include "TECTTL.h"
#include "AccelerometerProcess.h"
#include "ADCProcess.h"
#include "BalloonProcess.h"
#include <time.h>
#include <sys/mman.h>
#include <linux/pci.h>
#include <unistd.h>
#include <pwd.h>
#define MIN_ASCENT_RATE 100
#define DEBUG



typedef enum SBCstate_enum { boot, preflight, takeoff, cruising, falling } SBCstate; //SBC states

static __off_t get_fpga_phy(void);

void test() {
    //currently used as testbed
    true;
    //int* FPGAsyscon = (int*) 0xFC081000;
    //*(FPGAsyscon + 0x0c) &= ~(1 << 20);
    printf("hello from %s!\n", "ConsoleApplication1");
    int AccelFD = Accelerometer::accelerometer_init();
    //accelerometer_reset(AccelFD);
    //accelerometerSetNormalRead(AccelFD);
    uint16_t data[3];
    //getAcceration(AccelFD, data);
    printf("x = %d, y = %d, z =%d\n", data[0], data[1], data[2]);
    //*(FPGAsyscon + 0x0c) &= ~(1 < 20);
    return;
}

int main()
{   
    time_t bootTime, currentTime;
    SBCstate sbcState = boot;
    Accelerometer* accel;
    ADC* adc;
    TECTTL* tec;
    Balloon* balloon;
    float alitudeRate;
    bool motionInterupt;
    char testChar[256], testMsg[256];
    
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

    //int fdttyS7 = open("/dev/ttyS7", O_RDWR | O_SYNC);

    ////unsigned int* syscon2 = (unsigned int*)mmap(NULL, getpagesize(), PROT_READ | PROT_WRITE, MAP_SHARED, devmem, 0xE80000C0);

    //syscon[0xc / 4] |= (1 << 16);
    //syscon[0xC4 / 4] |= (1 << 4);
    //syscon[0xD4 / 4] |= (1 << 4);

    //int status = syscon[0xC4 / 4];
    //fprintf(stderr, "%d\n", status);
    //strcpy(testChar, "Can you hear me?");
    //write(fdttyS7, testChar, strlen(testChar)+1);
    //status = syscon[0xC4 / 4];
    //fprintf(stderr, "%d\n", status);
    //usleep(1000);
    //read(fdttyS1, testChar, 25);
    //fprintf(stderr, testChar);

    //fprintf(stderr, "new test");
#endif // DEBUG

   
    

    while (1) {//automata loop
        switch (sbcState) //state handler
        {
        case boot:
            accel = new Accelerometer();
            adc = new ADC(accel->twifd);

            //set /dev/ttts6 to auto TxEN
            syscon[0x4 / 4] &= ~(1 << (11 - 1)); //set DIO pin 11 to idle
            syscon[0x8 / 4] &= ~(1 << (11 - 1)); //set DIO pin 11 to out


            tec = new TECTTL();
//            tec->clearBuffer();
            tec->getPrintOut(testChar);
            balloon = new Balloon();

            accel->setMotionFreefallInterupt((float)1.25,0b100,true);
            accel->getAcceleration();

            tec->setParams(30, 1, 1, 1);
            tec->getPrintOut(testChar);

            adc->ADC_init();
            adc->getADC();

            bootTime = time(0); //this should be GMT/UTC, double check
            if (true && bootTime != .1)//boot check
                sbcState = preflight;
            break;
        case preflight:
            if(true)//time since last check > 1min
               motionInterupt = accel->checkMotionInteruptFlag(NULL);
            currentTime = time(0);

            syscon[(0xc / 4)] &= ~(1 << 20); //turn red led off
            syscon[(0xc / 4)] |= (1 << 20); //turn red led on

            strcpy(testMsg,"HelloBalloon\n\rNextMessagge\n\rcutoffMe");
            write(balloon->fdRS232, testMsg, sizeof(testMsg));
            strcpy(testMsg, "Message\n\rRandomNoise");
            write(balloon->fdRS232, testMsg, sizeof(testMsg));
            balloon->readBuf();

            tec->sendParams();
            tec->getPrintOut(testChar);


            if (alitudeRate > MIN_ASCENT_RATE || motionInterupt || currentTime - bootTime > 4 * 3600)
            {
                sbcState = takeoff;
                motionInterupt = false;
            }
            break;
        case takeoff:

            if (alitudeRate < MIN_ASCENT_RATE)
            {
                sbcState = cruising;
                accel->setMotionFreefallInterupt(.1, 0b100, false);
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