//
//  ConcreteIRCSPStates.h
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/5/21.
//
#include <iostream>
#include <stdexcept>


#pragma once
#include "IRCSPState.h"
#include "IRCSP.h"

//BOOT CLASS
class Boot : public IRCSPState
{
public:
    void enter(IRCSP* ircsp) {
        void check_telemetry(IRCSP* ircsp);
        std::cout << "Entering Boot State\n";
    }
    void toggle(IRCSP* ircsp);
    void exit(IRCSP* ircsp) {
    }
    static IRCSPState& getInstance();

private:
    Boot() {}
    Boot(const Boot& other);
    Boot& operator=(const Boot& other);
};

//PREFLIGHT CLASS
class Preflight : public IRCSPState
{
public:
    void enter(IRCSP* ircsp) {
        std::cout << "Entering Preflight State\n";
        void check_telemetry(IRCSP* ircsp);
    }
    void toggle(IRCSP* ircsp);
    void exit(IRCSP* ircsp) {
    
    }
    static IRCSPState& getInstance();

private:
    Preflight() {}
    Preflight(const Preflight& other);
    Preflight& operator=(const Preflight& other);
};

//TAKEOFF CLASS
class Takeoff : public IRCSPState
{
public:
    void enter(IRCSP* ircsp) {
        std::cout << "Entering Takeoff State\n";
    }
    void toggle(IRCSP* ircsp);
    void exit(IRCSP* ircsp) {
    
    }
    static IRCSPState& getInstance();
private:
    Takeoff() {}
    Takeoff(const Takeoff& other);
    Takeoff& operator=(const Takeoff& other);
};

//CRUISING CLASS
class Cruising : public IRCSPState
{
public:
    void enter(IRCSP* ircsp) {
        std::cout << "Entering Crusing State\n";
    }
    void toggle(IRCSP* ircsp);
    void exit(IRCSP* ircsp) {
    }
    static IRCSPState& getInstance();
    
private:
    Cruising() {}
    Cruising(const Cruising& other);
    Cruising& operator=(const Cruising& other);
};

//Falling CLASS
class Falling : public IRCSPState
{
public:
    void enter(IRCSP* ircsp) {
        std::cout << "Instrument in Freefall \n";
    }
    void toggle(IRCSP* ircsp);
    void exit(IRCSP* ircsp) {
    }
    static IRCSPState& getInstance();

private:
    Falling() {}
    Falling(const Falling& other);
    Falling& operator=(const Falling& other);
};


//SHUTDOWN CLASS
class Shutdown : public IRCSPState
{
public:
    void enter(IRCSP* ircsp) {
        std::cout << "Begining Shutdown\n";
    }
    void toggle(IRCSP* ircsp);
    void exit(IRCSP* ircsp) {
        std::cout << "Shutdown Complete\n";
    }
    static IRCSPState& getInstance();

private:
    Shutdown() {}
    Shutdown(const Shutdown& other);
    Shutdown& operator=(const Shutdown& other);
};

