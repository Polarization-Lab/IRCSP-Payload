#pragma once
#ifndef NTCTHERMISTORDECODER_H
#include "ADC.h"
#include <cmath>
#define NTCTHERMISTORDECODER_H

class NTCThermistorDecoder:public ADC //Thermistor decoder extends ADC
{
public:
	bool channels[5];
	void getTemp();
	void getTemp(float[5]);
	NTCThermistorDecoder(bool channels[5], const float sourceVoltage[5], const float resistors[5], const float refTemp[5], const float thermistorRefResistance[5], const float thermistorSensitivity[5][4]);
	NTCThermistorDecoder(int twifd, bool channels[5], const float sourceVoltage[5], const float resistors[5], const float refTemp[5], const float thermistorRefResistance[5], const float thermistorSensitivity[5][4]);
	~NTCThermistorDecoder();
protected:
	float temperatures[5]; //in K
private:
	float sourceVoltage[5];
	float resistors[5];
	float refTemp[5]; //in K
	float thermistorRefResistance[5];
	float thermistorSensitivity[5][4];
};

void NTCThermistorDecoder::getTemp()
{
	float resistanceRatio;
	getADC();
	for (int i = 0; i < 5; i++) {
		if (channels[i]) {
			resistanceRatio = (2*sourceVoltage[i] / voltages[i] - 2) * resistors[i]/thermistorRefResistance[i];
			temperatures[i] = 1 / (thermistorSensitivity[i][0] + thermistorSensitivity[i][1] * log(resistanceRatio) + thermistorSensitivity[i][2] * pow(log(resistanceRatio), 2) + thermistorSensitivity[i][3] * pow(log(resistanceRatio), 2));
		}
		else {
			temperatures[i] = -1;
		}
	}
}

inline void NTCThermistorDecoder::getTemp(float tempOut[5])
{
	getTemp();
	for (int i = 0; i < 5; i++)
		tempOut[i] = temperatures[i];
}

NTCThermistorDecoder::NTCThermistorDecoder(bool channels[5], const float sourceVoltage[5], const float resistors[5], const float refTemp[5], const float thermistorRefResistance[5], const float thermistorSensitivity[5][4])
{
	for (int i = 0; i < 5; i++) {
		this->channels[i] = channels[i];
		this->sourceVoltage[i] = sourceVoltage[i];
		this->resistors[i] = resistors[i];
		this->refTemp[i] = refTemp[i];
		this->thermistorRefResistance[i] = thermistorRefResistance[i];
		for (int j = 0; j < 4; j++) {
			this->thermistorSensitivity[i][j] = thermistorSensitivity[i][j];
		}
	}
}

inline NTCThermistorDecoder::NTCThermistorDecoder(int twifd, bool channels[5], const float sourceVoltage[5], const float resistors[5], const float refTemp[5], const float thermistorRefResistance[5], const float thermistorSensitivity[5][4]) : ADC(twifd)
{
	for (int i = 0; i < 5; i++) {
		this->channels[i] = channels[i];
		this->sourceVoltage[i] = sourceVoltage[i];
		this->resistors[i] = resistors[i];
		this->refTemp[i] = refTemp[i];
		this->thermistorRefResistance[i] = thermistorRefResistance[i];
		for (int j = 0; j < 4; j++) {
			this->thermistorSensitivity[i][j] = thermistorSensitivity[i][j];
		}
	}
}


NTCThermistorDecoder::~NTCThermistorDecoder()
{
}




#endif