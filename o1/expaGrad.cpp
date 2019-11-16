#include <math.h>
#include <iostream>
#include <cstdlib>


#define FDER0 -0.56284
#define BETA 0.5
#define KAPPA 0.0001

/*
double function(double x){
    double a = sin(2*x+1)+2;
    return 1 / (1 + exp(a));
}
*/

double function(double x){
    return sqrt(sin(exp(-2*x))+2);
}

int main(){

    double result;
    double f0 = function(0);
    double tau = 0;
    double prevtau = 0;

    if(function(tau) <= f0 + BETA*FDER0*tau){
        while(function(tau) <= f0 + BETA*FDER0*tau){
            tau += KAPPA;
        }
    }
    else{
        while(function(tau) > f0 + BETA*FDER0*tau){
            tau -= KAPPA;         
        }
    }
    printf("tau %lf\n", tau);
    


    result = function(tau);

    std::cout << "Minimum is: " << result << std::endl;

    return 0;
}