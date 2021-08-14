/* LCD 2x24 character example code
 *
 * To compile, copy to the board and run:
 * 	gcc lcd.c -o lcd  */

#include <stdio.h>
#include <stdint.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <time.h>

void lcd_init(void);
void lcd_wait(void);
void lcd_command(unsigned int cmd);
void lcd_writechars(unsigned char* dat);

// These are nanosecond delays
#define SETUP   800
#define PULSE   1600
#define HOLD    800

// The mpeek/mpoke functions are specific to the TS-47XX
volatile uint16_t* muxbus = 0;
int mem = 0;
uint16_t mpeek16(uint16_t addr)
{
    uint16_t value;
    if (mem == 0)
        mem = open("/dev/mem", O_RDWR | O_SYNC);

    if (muxbus == 0)
        muxbus = mmap(0,
            getpagesize(),
            PROT_READ | PROT_WRITE,
            MAP_SHARED,
            mem,
            0x80008000);

    return muxbus[addr / 2];
}

void mpoke16(uint16_t addr, uint16_t value)
{
    if (mem == 0)
        mem = open("/dev/mem", O_RDWR | O_SYNC);

    if (muxbus == 0)
        muxbus = mmap(0,
            getpagesize(),
            PROT_READ | PROT_WRITE,
            MAP_SHARED,
            mem,
            0x80008000);

    muxbus[addr / 2] = value;
}

void lcd_init(void) {
    uint16_t out;
    // Data lines to inputs, control lines to outputs
    mpoke16(0xa, 0x700);

    out = mpeek16(0x6);
    // Set LCD_EN and LCD_RS low
    out &= ~(0x600);
    // Set LCD_WR high
    out |= 0x100;
    mpoke16(0x6, out);

    usleep(15000);
    lcd_command(0x38); // two rows, 5x7, 8 bit
    usleep(4100);
    lcd_command(0x38); // two rows, 5x7, 8 bit
    usleep(100);
    lcd_command(0x38); // two rows, 5x7, 8 bit
    lcd_command(0x6); // cursor increment mode
    lcd_wait();
    lcd_command(0x1); // clear display
    lcd_wait();
    lcd_command(0xc); // display on, blink off, cursor off
    lcd_wait();
    lcd_command(0x2); // return home
}

void lcd_wait(void) {
    uint16_t ddr, out, in;
    int i, dat, tries = 0;
    struct timespec dly;
    dly.tv_sec = 0;

    mpoke16(0xa, mpeek16(0xa) & 0xff00);
    out = mpeek16(0x6);

    do {
        // step 1, apply RS & WR
        out |= 0x100; // de-assert WR
        out &= ~0x200; // de-assert RS
        mpoke16(0x6, out);

        // step 2, wait
        dly.tv_nsec = SETUP;
        nanosleep(&dly, NULL);

        // step 3, assert EN
        out |= 0x400;
        mpoke16(0x6, out);

        // step 4, wait
        dly.tv_nsec = PULSE;
        nanosleep(&dly, NULL);

        // step 5, de-assert EN, read result
        in = mpeek16(0xe) & 0xff;
        out &= ~0x400; // de-assert EN
        mpoke16(0x6, out);

        // step 6, wait
        dly.tv_nsec = HOLD;
        nanosleep(&dly, NULL);
    } while (in & 0x80 && tries++ < 1000);
}

void lcd_command(unsigned int cmd) {
    int i;
    uint16_t out;
    struct timespec dly;
    dly.tv_sec = 0;

    // Set port A to outputs
    mpoke16(0xa, mpeek16(0xa) | 0x00ff);
    out = mpeek16(0x6);

    // step 1, apply RS & WR, send data
    out &= 0xff00;
    out |= (cmd & 0xff);
    out &= ~(0x300); // de-assert RS, assert WR
    mpoke16(0x6, out);

    // step 2, wait
    dly.tv_nsec = SETUP;
    nanosleep(&dly, NULL);

    // step 3, assert EN
    out |= 0x400;
    mpoke16(0x6, out);

    // step 4, wait
    dly.tv_nsec = PULSE;
    nanosleep(&dly, NULL);

    // step 5, de-assert EN 
    out &= ~0x400;
    mpoke16(0x6, out);

    // step 6, wait 
    dly.tv_nsec = HOLD;
    nanosleep(&dly, NULL);
}

void lcd_writechars(unsigned char* dat) {
    int i;
    uint16_t out = mpeek16(0x6);
    struct timespec dly;
    dly.tv_sec = 0;

    do {
        lcd_wait();

        // set data lines to outputs
        mpoke16(0xa, mpeek16(0xa) | 0x00ff);

        // step 1, apply RS & WR, send data
        out &= 0xff00;
        out |= *dat++;
        out |= 0x200; // assert RS
        out &= ~0x100; // assert WR
        mpoke16(0x6, out);

        // step 2
        dly.tv_nsec = SETUP;
        nanosleep(&dly, NULL);

        // step 3, assert EN
        out |= 0x400;
        mpoke16(0x6, out);

        // step 4, wait 800 nS
        dly.tv_nsec = PULSE;
        nanosleep(&dly, NULL);

        // step 5, de-assert EN 
        out &= ~0x400;
        mpoke16(0x6, out);

        // step 6, wait
        dly.tv_nsec = HOLD;
        nanosleep(&dly, NULL);
    } while (*dat);
}

int mainLCD(int argc, char** argv)
{
    int i = 0;

    lcd_init();
    if (argc == 2) {
        lcd_writechars(argv[1]);
    }
    if (argc > 2) {
        lcd_writechars(argv[1]);
        lcd_wait();
        lcd_command(0xa8); // set DDRAM addr to second row
        lcd_writechars(argv[2]);
    }
    if (argc >= 2) return 0;

    while (!feof(stdin)) {
        unsigned char buf[512];

        lcd_wait();
        if (i) {
            // XXX: this seek addr may be different for different
            // LCD sizes!  -JO
            lcd_command(0xa8); // set DDRAM addr to second row
        }
        else {
            lcd_command(0x2); // return home
        }
        i = i ^ 0x1;
        if (fgets(buf, sizeof(buf), stdin) != NULL) {
            unsigned int len;
            buf[0x27] = 0;
            len = strlen(buf);
            if (buf[len - 1] == '\n') buf[len - 1] = 0;
            lcd_writechars(buf);
        }
    }
    return 0;
}