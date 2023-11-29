#include<iostream>
#include<cstdlib>
using namespace std;

int main(){


    srand((unsigned) time(NULL));

    int random = 1 + (rand() % 31);

    cout<<random<<endl;

    return random;

}
