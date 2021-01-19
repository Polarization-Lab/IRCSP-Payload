/*  Copyright 2011-2017, Unpublished Work of Technologic Systems
 *  All Rights Reserved.
 *
 *  THIS WORK IS AN UNPUBLISHED WORK AND CONTAINS CONFIDENTIAL,
 *  PROPRIETARY AND TRADE SECRET INFORMATION OF TECHNOLOGIC SYSTEMS.
 *  ACCESS TO THIS WORK IS RESTRICTED TO (I) TECHNOLOGIC SYSTEMS EMPLOYEES
 *  WHO HAVE A NEED TO KNOW TO PERFORM TASKS WITHIN THE SCOPE OF THEIR
 *  ASSIGNMENTS  AND (II) ENTITIES OTHER THAN TECHNOLOGIC SYSTEMS WHO
 *  HAVE ENTERED INTO  APPROPRIATE LICENSE AGREEMENTS.  NO PART OF THIS
 *  WORK MAY BE USED, PRACTICED, PERFORMED, COPIED, DISTRIBUTED, REVISED,
 *  MODIFIED, TRANSLATED, ABRIDGED, CONDENSED, EXPANDED, COLLECTED,
 *  COMPILED,LINKED,RECAST, TRANSFORMED, ADAPTED IN ANY FORM OR BY ANY
 *  MEANS,MANUAL, MECHANICAL, CHEMICAL, ELECTRICAL, ELECTRONIC, OPTICAL,
 *  BIOLOGICAL, OR OTHERWISE WITHOUT THE PRIOR WRITTEN PERMISSION AND
 *  CONSENT OF TECHNOLOGIC SYSTEMS . ANY USE OR EXPLOITATION OF THIS WORK
 *  WITHOUT THE PRIOR WRITTEN CONSENT OF TECHNOLOGIC SYSTEMS  COULD
 *  SUBJECT THE PERPETRATOR TO CRIMINAL AND CIVIL LIABILITY.
 */
/* To compile eth_phy_peekpoke, use the appropriate cross compiler and run the
 * command:
 *
 *   gcc -Wall -O -mcpu=arm9 -o eth_phy_peekpoke eth_phy_peekpoke.c 
 *
 * On uclibc based initrd's, the following additional gcc options are
 * necessary: -Wl,--rpath,/slib -Wl,-dynamic-linker,/slib/ld-uClibc.so.0
 */
 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <assert.h>
#include <getopt.h>
#include <sys/mman.h>
#include <signal.h>

static volatile unsigned long *neta_base;
static volatile int timed_out;

#define NETA_BASE          0xf1072000 /* ethernet@70000 */
#define SMI_REG_OFFSET         0x0004

#define SMI_RDVALID     (1 << 27)
#define SMI_BUSY        (1 << 28)


static int smi_read(unsigned long phy, unsigned long reg, unsigned short *data) {
 
   unsigned long x;
   
   alarm(1);
   while(neta_base[SMI_REG_OFFSET / 4] & SMI_BUSY) 
      if(timed_out) return -1;            
         
   neta_base[SMI_REG_OFFSET / 4] = (phy << 16) | (reg << 21) | (1 << 26); 
        
   while(neta_base[SMI_REG_OFFSET / 4] & SMI_BUSY)
      if(timed_out) return -1;
      
   while(! ((x = neta_base[SMI_REG_OFFSET / 4]) & SMI_RDVALID)) 
      if(timed_out) return -1;
   
   *data = x & 0xFFFF;
      
   return 0;
}

static int smi_write(unsigned long phy, unsigned long reg, unsigned short data) {
 
   alarm(1);
   while(neta_base[SMI_REG_OFFSET / 4] & SMI_BUSY)
      if(timed_out) return -1;
           
   neta_base[SMI_REG_OFFSET / 4] = (phy << 16) | (reg << 21) | data;
      
   while(neta_base[SMI_REG_OFFSET / 4] & SMI_BUSY) 
      if(timed_out) return -1;
      
   return 0;   
}



static int phy_read(unsigned long phy, unsigned long reg, unsigned short *data) 
{ 
   return smi_read(phy, reg, data);   
}

static int phy_write(unsigned long phy, unsigned long reg, unsigned short data) 
{
   return smi_write(phy, reg, data);
}

static void timeout_handler(int signum) {   
   timed_out = 1;
	signal(signum, timeout_handler);
}


static void usage(char **argv) {
	fprintf(stderr, "Usage: %s PHY REG [data [x]]\n"
	  "Technologic Systems Ethernet PHY access utility for the TS-7800-V2\n"
	  "\n"	  
	  "  PHY    Specify PHY address\n"	  
	  "  REG    Specify register to read (or write)\n"
     "  data   Optional data to write\n"
     "  x      Can be anything; supresses read-back on write\n",
	  argv[0]
	);
}


int main(int argc, char*argv[]) {
   int devmem;
   unsigned short data = 0;   
   int c;
   unsigned char opt_phy = 0, opt_reg = 0;
   int opt_write = 0;
   int have_reg = 0, have_phy = 0;
   
   
   if (argc < 3) {
      usage(argv);
      return 1;      
   }
   
	for(c=1; c < argc; c++) {
	   switch(c) {
	   case 1:
	      opt_phy = (unsigned char)strtoul(argv[1], NULL, 0);
	      if (opt_phy < 0 || opt_phy > 31) {
	         fprintf(stderr,  "PHY out of range [0..31]\n");
	         usage(argv);
	         return 1;
	      }
	      have_phy = 1;
	      break;
	      
	   case 2:
	      opt_reg = (unsigned char)strtoul(argv[2], NULL, 0);
	      if (opt_reg < 0 || opt_reg > 31) {
	         fprintf(stderr,  "REG out of range [0..31]\n");
	         usage(argv);
	         return 1;
	      }
	      have_reg = 1;
	      break;
	      
	   case 3:
	      data = (unsigned short)strtoul(argv[3], NULL, 0);
	      opt_write = 1;	      
	   }	   
	}
   
	if (!have_phy) {
	   fprintf(stderr, "Error:  Must specify a PHY address [0..31]\n");
	   return 1;
	} 
	
	if (!have_reg) {
	   fprintf(stderr, "Error:  Must specify a REG address [0..31]\n");
	   return 1;
	} 
	
	if ((devmem = open("/dev/mem", O_RDWR|O_SYNC)) < 0) {
	   fprintf(stderr, "Error: Can't open /dev/mem\n");
	   return 1;
	}
					
   if ((neta_base = mmap(0, 4096, PROT_READ | PROT_WRITE, MAP_SHARED, 
         devmem, NETA_BASE)) == MAP_FAILED) {
      fprintf(stderr, "Error: Can't mmap 0x%08lX\n", (unsigned long)NETA_BASE);
      return 1;
   }
      
   signal(SIGALRM, timeout_handler); 
   
   if (opt_write) {      
      if (phy_write(opt_phy, opt_reg, data) < 0) {
         fprintf(stderr, "Error: Timeout writing to register #%d\n", opt_reg);
	   return 1;
      }
   } 
   
   if (argc < 5) {
      if (phy_read(opt_phy, opt_reg, &data) < 0) {
         fprintf(stderr, "Error: Timeout reading from register #%d\n", opt_reg);
         return 1;
      }
      
      printf("0x%04X\n", data);
   }
      
   return 0;   
}
