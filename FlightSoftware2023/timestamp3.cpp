#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    
    srand((unsigned) time(NULL));

    int random = (rand() % 59);

    cout << random << endl;

    return random;

}
