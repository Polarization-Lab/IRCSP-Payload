#include "TECTTL.h"
#include <string>
#include <cstdlib>
using namespace std;

void TECTTL::sendParams() {
	string message = "< " + to_string(setpoint);
}