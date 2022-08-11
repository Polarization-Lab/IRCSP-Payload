//
//  ConcreteIRCSPStates.h
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/5/21.
//  Edited by Jaclyn John on 6/20/22
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


//FLIGHT CLASS
class Flight : public IRCSPState
{
public:
    void enter(IRCSP* ircsp) {
        std::cout << "Entering Flight State\n";
        
    }
    void toggle(IRCSP* ircsp);
    void exit(IRCSP* ircsp) {
    
    }
    static IRCSPState& getInstance();
private:
    Flight() {}
    Flight(const Flight& other);
    Flight& operator=(const Flight& other);
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
