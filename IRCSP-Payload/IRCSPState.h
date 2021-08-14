//
//  IRCSPState.h
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/5/21.
//

#pragma once
#include "IRCSP.h"

// Forward declaration to resolve circular dependency/include
class IRCSP;

class IRCSPState
{
public:
    virtual void enter(IRCSP* ircsp) = 0;
    virtual void toggle(IRCSP* ircsp) = 0;
    virtual void exit(IRCSP* ircsp) = 0;
    virtual ~IRCSPState() {}
};
