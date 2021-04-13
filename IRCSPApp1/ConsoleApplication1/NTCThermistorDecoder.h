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
	NTCThermistorDecoder(bool channels[5], const float sourceVoltage[5], const float resistors[5], const float refTemp[5], const float thermistorRefResistance[5], const float thermistorSensitivity[5]);
	NTCThermistorDecoder(int twifd, bool channels[5], const float sourceVoltage[5], const float resistors[5], const float refTemp[5], const float thermistorRefResistance[5], const float thermistorSensitivity[5]);
	~NTCThermistorDecoder();
protected:
	float temperatures[5]; //in K
private:
	float sourceVoltage[5];
	float resistors[5];
	float refTemp[5]; //in K
	float thermistorRefResistance[5];
	float thermistorSensitivity[5];
};

void NTCThermistorDecoder::getTemp()
{
	getADC();
	for (int i = 0; i < 5; i++) {
		if (channels[i]) {
			temperatures[i] = (refTemp[i] + 273) * thermistorSensitivity[i] / (thermistorSensitivity[i] + log(((sourceVoltage[i] - voltages[i]) * resistors[i] / (thermistorRefResistance[i] * voltages[i])))); //Vin/Vref = R2/(Rth + R2) //Rth = R0*exp(beta*(1/(T)-1/(T0)) Temp in K
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

NTCThermistorDecoder::NTCThermistorDecoder(bool channels[5], const float sourceVoltage[5], const float resistors[5], const float refTemp[5], const float thermistorRefResistance[5], const float thermistorSensitivity[5])
{
	for (int i = 0; i < 5; i++) {
		this->channels[i] = channels[i];
		this->sourceVoltage[i] = sourceVoltage[i];
		this->resistors[i] = resistors[i];
		this->refTemp[i] = refTemp[i];
		this->thermistorRefResistance[i] = thermistorRefResistance[i];
		this->thermistorSensitivity[i] = thermistorSensitivity[i];
	}
}

inline NTCThermistorDecoder::NTCThermistorDecoder(int twifd, bool channels[5], const float sourceVoltage[5], const float resistors[5], const float refTemp[5], const float thermistorRefResistance[5], const float thermistorSensitivity[5]) : ADC(twifd)
{
	for (int i = 0; i < 5; i++) {
		this->channels[i] = channels[i];
		this->sourceVoltage[i] = sourceVoltage[i];
		this->resistors[i] = resistors[i];
		this->refTemp[i] = refTemp[i];
		this->thermistorRefResistance[i] = thermistorRefResistance[i];
		this->thermistorSensitivity[i] = thermistorSensitivity[i];
	}
}


NTCThermistorDecoder::~NTCThermistorDecoder()
{
}




#endif