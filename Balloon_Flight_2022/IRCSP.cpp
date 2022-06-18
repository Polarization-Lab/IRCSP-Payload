//
//  IRCSP.cpp
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/5/21.
//

#include "IRCSP.h"
#include <iostream>
#include <sstream>
#include <fstream>

//#include "Accelerometer.h"

IRCSP::IRCSP()
{

}

void IRCSP::check_telemetry (time_t bootTime)
{

    time_elapsed = time(NULL) - bootTime;
    
    //temperatures
    t_sbc =  GetStdoutFromCommand("ts7800ctl -t " );
    
    //get data space
    dataspace = GetStdoutFromCommand("du -k " + dataPath);
    
    //camera temperatures from .txt file
    std::fstream myfile1("/mnt/sdcard/image_data/temp1.txt", std::ios_base::in);
    myfile1 >> cam1_t;
    std::fstream myfile2("/mnt/sdcard/image_data/temp2.txt", std::ios_base::in);
    myfile2 >> cam2_t;
    
    //BME280 readings from .txt file
    std::fstream myfile3("/mnt/sdcard/image_data/hum.txt", std::ios_base::in);
    myfile3 >> humidity;
    std::fstream myfile4("/mnt/sdcard/image_data/temp.txt", std::ios_base::in);
    myfile4 >> t_ircsp;
    std::fstream myfile5("/mnt/sdcard/image_data/pres.txt", std::ios_base::in);
    myfile5 >> pressure;
    
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
