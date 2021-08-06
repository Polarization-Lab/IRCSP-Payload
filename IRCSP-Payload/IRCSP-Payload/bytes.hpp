//
//  bytes.hpp
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/6/21.
//

#ifndef bytes_hpp
#define bytes_hpp

#include <string.h>
#include <math.h>   // For POW function

int toInt( unsigned char mybyte);  // Single ASCII Hex caracter

int hex_to_int(char *str);  // BYTE in ASCII HEX

long hex_to_long(char *str);  // Long in ASCII HEX

#endif /* bytes_hpp */
