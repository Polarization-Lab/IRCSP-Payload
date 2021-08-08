//
//  IRCSP.cpp
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/5/21.
//

#include "IRCSP.h"
#include "ConcreteIRCSPStates.h"
#include <iostream>
#include <sstream>

//#include "Accelerometer.h"

IRCSP::IRCSP()
{
    // All lights are initially turned off
    currentState = &Boot::getInstance();
}

void IRCSP::setState(IRCSPState& newState)
{
    currentState->exit(this);  // do stuff before we change state
    currentState = &newState;  // actually change states now
    currentState->enter(this); // do stuff after we change state
}

void IRCSP::toggle()
{
    // Delegate the task of determining the next state to the current state
    currentState->toggle(this);
}


void IRCSP::check_telemetry (time_t bootTime, Accelerometer& accelerometer, TEC& tec )
{
    accelerometer.getAcceleration();
    
    
    time_elapsed = time(NULL) - bootTime;
    acceleration = accelerometer.total_accel;
    t_sbc = 1; // GetStdoutFromCommand("ts7800ctl -t " );
    t_ircsp = 1;
    
    //get data space
    dataspace = GetStdoutFromCommand("du -k " + dataPath);
}

void IRCSP::set_PID (long temp)
{
    PID_target = temp;
    //TODO: add function setting PID parameteres
}

int IRCSP::GetStdoutFromCommand(std::string cmd) {

  std::string data;
  FILE * stream;
  const int max_buffer = 256;
  char buffer[max_buffer];
  cmd.append(" 2>&1");

  stream = popen(cmd.c_str(), "r");
  if (stream) {
    while (!feof(stream))
      if (fgets(buffer, max_buffer, stream) != NULL) data.append(buffer);
    pclose(stream);
  }
  std::stringstream ss;
  /* Storing the whole string into string stream */
  ss << data;
  std::string temp;
  int found = 0;
  while (!ss.eof()) {
    ss >> temp;
      if (std::stringstream(temp) >> found){
        return found;
      }
  }
  return found;
}



