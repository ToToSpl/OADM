#include <math.h>
#include <iostream>
#include <cstdlib>

#define F0 -0.56284
#define EPSILON 1.0
#define CYCLES 50

float leftBorder = -1;
float rightBorder = 1;

/*
float function(float x){
    float sin = sinf(2*x+1)+2;
    return 1 / (1 + expf(sin));
}
*/



float function(float x){
    return powf(x,2);
}


float fib(int n){
    if (n == 0 || n == 1)
        return 1;

    return fib(n - 1) + fib(n - 2);
}

float calcD(int n){
    return (fib(n-1)/fib(n))*(2) + (powf(-1,n)/fib(n))*EPSILON;
    //return (fib(CYCLES - n) / fib(CYCLES)) * (rightBorder - leftBorder);
}

float calculate(float a, float b) {
    float left, right;

    for (int i = 1; i < CYCLES; i++) {
        left = fib(CYCLES - i - 1)/fib(CYCLES - i + 1)*(b - a) + a;
        right = fib(CYCLES - i)/fib(CYCLES - i + 1)*(b - a) + a;
        
        if (function(right) > function(left)) {
            b = right;
        } else
        {
            a = left;
        }

    return function((a+b)/2);
    }
}


int main(){
    /*
    float x1,x2, result, tempD;

    for(int i = 1; i < CYCLES + 1; i++){
        //calculate x1 and x2
        tempD = calcD(i);
        //if(tempD <= EPSILON){printf("BREAK\n"); break;}
        x1 = leftBorder - tempD; x2 = rightBorder + tempD;

        if(function(x1) >= function(x2)){
            leftBorder = x1;
        }else{
            rightBorder = x2;
        }
    }*/

    float result = calculate(-1, 1);
    printf("x = %d\nMinimum = %lf\n", 12121212, result);

    return 0;
}

