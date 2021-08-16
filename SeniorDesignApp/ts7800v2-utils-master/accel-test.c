#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <signal.h>
#include <sys/select.h>
#include <linux/input.h>


/*
   Test the MMA8451 device.

   The mma8451 driver must be loaded before running this code.

*/

#define INPUT_DEVICE "/dev/input/event0"

//---------------------------------

static int running;
static int ev;

int get_accel_ev(int *myx,int *myy, int *myz)
{
  fd_set fds;
  struct timeval t;
  struct input_event event;
  static int x, y, z;
  double rx,ry,rz;

  FD_ZERO(&fds);
  FD_SET(ev,&fds);
  t.tv_sec = 0;
  t.tv_usec = 0;
  while (select(ev+1,&fds,NULL,NULL,&t)) {
     if (! running) return 0;
    read(ev,&event,sizeof(event));
    switch (event.type) {
    case EV_REL:
      switch (event.code) {
      case REL_X:
         *myx = x = event.value;
         rx = (double)x / 4096.0;
         printf("EV_REL:X=%#0.03g\n", rx);
         break;
      case REL_Y:
         *myy = y = event.value;
         ry = (double)y / 4096.0;
         printf("EV_REL:Y=%#0.03g\n", ry);
         break;
      case REL_Z:
         *myz = z = event.value;
         rz = (double)z / 4096.0;
         printf("EV_REL:Z:=%#0.03g\n", rz);
         break;
      default:
         printf("EV_REL code %d\n",event.code);
         break;
      }
      break;
   case EV_ABS:
      switch (event.code) {
         case ABS_X:
            x = event.value;
            rx = (double)x / 4096.0;
            printf("ABS_X=%#0.03g\n", rx);
            break;
         case ABS_Y:
             y = event.value;
             ry = (double)y / 4096.0;
             printf("ABS_Y=%#0.03g\n", ry);
            break;
         case ABS_Z:
            z = event.value;
            rz = (double)z / 4096.0;
            printf("ABS_Z=%#0.03g\n", rz);
            break;

         default:
            printf("EV_ABS code %d\n",event.code);
            break;
      }
      break;

    case EV_SYN:
       //printf("EV_SYN\n");
       break;
    default:
         printf("Unhandled Event code %d\n",event.code);
      break;
    }
  }
  return 0;
}


static void sigint_handler(int signum)
{
   running = 0;
   signal(signum, sigint_handler);
}


int main (int argc, char **argv)
{
  int x,y,z;

  ev = open(INPUT_DEVICE, O_RDONLY);
  if (ev < 0) {
     perror("open " INPUT_DEVICE);
     return 1;
  }

  signal(SIGINT, sigint_handler); // Interrupt, catches Ctrl C
  signal(SIGTERM, sigint_handler); // Terminate
  signal(SIGHUP, sigint_handler); // Hangup.
  running = 1;
  while (running) {
     get_accel_ev(&x, &y, &z);
  }

  return 0;
}

