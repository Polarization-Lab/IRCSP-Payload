/*#include "UARTserial.h"
#include <fcntl.h>
#include <string.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>

int test(void) {
	int ttts6 = initTTLDIO();
	long int wr, rd;
	char* buffer;
	wr = write(ttts6, "hello world", 11);
	rd = read(ttts6, buffer, 11);
	printf(buffer);
	
	return 0;

}
*/
