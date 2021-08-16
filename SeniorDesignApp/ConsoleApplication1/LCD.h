#ifndef LCD_H
#define LCD_H
// LCD 2x24 character example code
 
#define PortA 0x3FC0
#define RS 0x3

#include <stdio.h>
#include <stdint.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <time.h>

class LCD
{
public:
    LCD();
    ~LCD();

    void fourBitCommandWithDelay(unsigned char data, unsigned int delay);
    volatile uint16_t* muxbus = 0;
    int mem = 0;

private:

};

LCD::LCD()
{
    mem = open("/dev/mem", O_RDWR | O_SYNC);
    muxbus = mmap(0, getpagesize(), PROT_READ | PROT_WRITE, MAP_SHARED, mem, 0e8000004);
    muxbus[1] &= ~(0xFF00);
}

LCD::~LCD()
{
}

void LCD::fourBitCommandWithDelay(unsigned char data, unsigned int delay) {
    *muxbus = (0x00FF & *muxbus) | (0xFF00 & data << 16);

}


#endif