utils = eth_phy_peekpoke led7800 peekpoke rtc7800 ts7800ctl load_fpga_flash \
 accel-test pwmctl idleinject

CC ?= arm-marvell-linux-uclibcgnueabi-gcc
CFLAGS =  -Wall -O -lprocps

all:  $(utils)

ts7800ctl: ts7800ctl.c gpiolib.c gpiolib.h

idleinject: idleinject.c

clean:
	rm -f $(utils)


