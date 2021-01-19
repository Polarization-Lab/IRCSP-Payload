#define _GNU_SOURCE         /* See feature_test_macros(7) */
#include <errno.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/time.h>
#include <signal.h>
#include <getopt.h>

#include "i2c-dev.h"

static int i2c_fd;

static void led_init(void);
static int get_gled(void);
static void set_gled(int);
static void offleds(void);
static void blink(int sig);
static int silabs_init(void);
static void sigint_handler(int signum);

static int done;
static int green_ticks = 10;
static int red_ticks = 10;
static int green_left,red_left;

// This runs in the background while testing/burnin and always giving 
// indication the CPU is alive by blinking both the red and green LEDs
// twice per second.  

void usage(char **argv) {
	fprintf(stderr, "Usage: %s [OPTION] ...\n"
	  "  -o, --offset      TBD\n"
	  "  -r, --red ticks   Blink the red LED at 'ticks' interval\n"
	  "  -g, --green ticks Blink the green LED at 'ticks' interval\n"
	  "  -h, --help        This help\n", 
	  program_invocation_short_name
	   );
}

int main(int argc, char **argv) 
{
   struct itimerval itv;
   int c,offset=0;
   static struct option long_options[] = {
      { "offset", required_argument, 0, 'o' },
      { "red", required_argument, 0, 'r' },
      { "green", required_argument, 0, 'g' },
      { 0, 0, 0, 0 }
   };
   led_init();  
   offleds();

   while((c = getopt_long(argc, argv, "r:g:o:", long_options,NULL)) != -1) {
      switch (c) {
         case 'g':
            green_ticks = atoi(optarg);
            break;
         case 'r':
            red_ticks = atoi(optarg);
            break;
         case 'o':
            offset = atoi(optarg);
            break;
         case 'h':
         default:
            usage(argv);
            return 0;
      }
   }
  green_left = green_ticks;
  red_left = red_ticks + offset;

   signal(SIGINT, sigint_handler); // Interrupt, catches Ctrl-C
   signal(SIGTERM, sigint_handler); // Terminate
   signal(SIGQUIT, sigint_handler); // Quit

   signal(SIGALRM, blink);
   signal(SIGUSR1, blink);
   signal(SIGHUP, blink);
   atexit(offleds);
   itv.it_interval.tv_sec = 0;
   itv.it_interval.tv_usec = 10000;
   itv.it_value.tv_sec = 0;
   itv.it_value.tv_usec = 10000;
   setitimer(ITIMER_REAL, &itv, NULL);

   while(!done) sleep(1);
   offleds();
   return 0;
}


static void sigint_handler(int signum) 
{
   done=1;
   printf("done\n");
	signal(signum, sigint_handler);
}

// LED stuff -------------------------------------------------------
static volatile unsigned int *gled = NULL;
static volatile unsigned int *rled = NULL;

static void led_init(void) 
{
  off_t page;
  unsigned char *syscon;
  int  fd = open("/dev/mem", O_RDWR|O_SYNC);
  const int SYSCON = 0xFC081000;

  if (fd == -1) {
    perror("/dev/mem");
    return;
  }
	    
  page = SYSCON & 0xfffff000;
  syscon = mmap(0, getpagesize(), PROT_READ|PROT_WRITE,MAP_SHARED, fd, page);
  
  if (syscon == MAP_FAILED) {
    perror("mmap:");    
  } else {
      gled = (unsigned int *)(syscon + (SYSCON & 0xfff) + 8);
      *gled &= ~(1 << 30);
      
      rled = (unsigned int *)(syscon + (SYSCON & 0xfff) + 0xc);
      *rled &= ~(1 << 20);
      
  }
   
  i2c_fd = silabs_init(); 
}


static int get_gled(void) 
{
  if (gled) {
    return (*gled & (1 << 30)) != 0;
  } else 
    
   {
    return 0;
  } 
}

static void set_gled(int on) 
{
  if (gled) {
    if (on) {
      *gled |= (1 << 30);
    } else {
      *gled &= ~(1 << 30);
    }
  } 
}

void set_rled(int on) 
{
  if (rled) {
    if (on) {
      *rled |= (1 << 20);
    } else {
      *rled &= ~(1 << 20);
    }
  } 
}

static void offleds(void) 
{ 
   set_gled(0); 
   set_rled(0); 
}


static void blink(int sig) 
{
  struct itimerval itv;
  static int rled = 0;  
  
  if (done) exit(0);
  
  if (green_left > 0) green_left--;
  if (red_left > 0) red_left--;

  if (red_left == 0) {
    red_left = red_ticks;
    rled = !rled;
    set_rled(rled);
  }
  if (green_left == 0) {
    green_left = green_ticks;
    set_gled(!get_gled());
  }

  
  // We shouldn't have to do the following, but if we don't we never see a second signal!

  itv.it_interval.tv_sec = 0;
  itv.it_interval.tv_usec = 10000;
  itv.it_value.tv_sec = 0;
  itv.it_value.tv_usec = 10000;
  setitimer(ITIMER_REAL, &itv, NULL);

  signal(sig, blink);

}

static int silabs_init(void)
{
	static int fd = -1;
	fd = open("/dev/i2c-0", O_RDWR);
	if(fd != -1) {
		if (ioctl(fd, I2C_SLAVE_FORCE, 0x4a) < 0) {
			perror("Microcontroller did not ACK 0x4a\n");
			return -1;
		}
	}

	return fd;
}
