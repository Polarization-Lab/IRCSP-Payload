//
//  IRCSP.cpp
//  IRCSP-Payload
//
//  Created by Kira Hart on 8/5/21.
//  Edited by Jaclyn John on 6/20/22
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
    std::fstream myfile1("/mnt/sdcard/image_data/FPAtemp1.txt", std::ios_base::in);
    myfile1 >> t_cam1;
    std::fstream myfile2("/mnt/sdcard/image_data/FPAtemp2.txt", std::ios_base::in);
    myfile2 >> t_cam2;
    std::fstream myfile3("/mnt/sdcard/image_data/FPAtemp3.txt", std::ios_base::in);
    myfile3 >> t_cam3;
    
    //BME280 readings from .txt file
    std::fstream myfile4("/mnt/sdcard/image_data/hum1.txt", std::ios_base::in);
    myfile4 >> ircsp_humidity;
    std::fstream myfile5("/mnt/sdcard/image_data/temp1.txt", std::ios_base::in);
    myfile5 >> t_ircsp;
    std::fstream myfile6("/mnt/sdcard/image_data/press1.txt", std::ios_base::in);
    myfile6 >> ircsp_pressure;
    std::fstream myfile7("/mnt/sdcard/image_data/hum2.txt", std::ios_base::in);
    myfile7 >> amb_humidity;
    std::fstream myfile8("/mnt/sdcard/image_data/temp2.txt", std::ios_base::in);
    myfile8>> t_amb;
    std::fstream myfile9("/mnt/sdcard/image_data/press2.txt", std::ios_base::in);
    myfile9 >> amb_pressure;
    std::fstream myfile10("/mnt/sdcard/image_data/hum3.txt", std::ios_base::in);
    myfile10 >> elec_humidity;
    std::fstream myfile11("/mnt/sdcard/image_data/temp3.txt", std::ios_base::in);
    myfile11 >> t_elec;
    std::fstream myfile12("/mnt/sdcard/image_data/press3.txt", std::ios_base::in);
    myfile12 >> elec_pressure;
    std::fstream myfile13("/mnt/sdcard/image_data/thermVal.txt", std::ios_base::in);
    myfile13 >> thermVal;
    std::fstream myfile14("/mnt/sdcard/image_data/contextVal.txt", std::ios_base::in);
    myfile14 >> contextVal;
    std::fstream myfile15("/mnt/sdcard/image_data/lensVal.txt", std::ios_base::in);
    myfile15 >> lensVal;
    std::fstream myfile15("/mnt/sdcard/image_data/thermtemp1.txt", std::ios_base::in);
    myfile15 >> therm_temp;
    std::fstream myfile15("/mnt/sdcard/image_data/context_temp.txt", std::ios_base::in);
    myfile15 >> context_temp;
    
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
