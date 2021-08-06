//
//  TEC.hpp
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/6/21.
//

#ifndef TEC_hpp
#define TEC_hpp

#include <stdio.h>

class TEC
{
public:
    float set_temp;
    int twifd;
    

    TEC(); //creates new object
    TEC(int twifd);
    ~TEC(); //destorys object
    
    
    void setTEC(float); 
    
    
private:
    
    
};

#endif /* TEC_hpp */
