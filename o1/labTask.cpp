#include <cstdlib>
#include <cmath>
#include <iostream>

//QUADRATIC APPROX
#define ACCURACY 0.01
double a = -1;
double b = 1;

double function1(double x){
    double s = sin(2*x+1)+2;
    return 1 / (1 + exp(s));
}

double function2(double x){
    return -sin(x+1);
}

double qudratApprox(double x1, double(*func)(double)){
    double x2;
    x2 = (func(a)*(pow(b,2) - pow(x1,2)) + func(x1)*(pow(a,2) - pow(b,2)) + func(b)*(pow(x1,2) - pow(a,2)))/
        (func(a)*(b-x1) + func(x1)*(a-b) + func(b)*(x1-a));
    x2 *= 0.5;

    if(a < x2 && b > x2){
        
        return x2;
    }else{
        std::cout<< "ERROR HAS OCCURED\n";
    }
    return x2;
}


int main(){

    double x = 0;

    double x2 = 1000;

    do{

        x2 = qudratApprox(x,function1);
        //std::cout << x2 << std::endl;

        if(function1(x) > function1(x2)){
            if(x < x2)  a = x;
            else b = x;
        }else{
            if(x < x2)  a = x2;
            else b = x2;
        }
        x = (a+b)/2;
        std::cout << "x = " << x << std::endl;

    }while(abs(x-x2) >= ACCURACY);

    std::cout << "xmin = " << x << std::endl;
    std::cout << "f(xmin) = " << function1(x) << std::endl;

    return 1;
}