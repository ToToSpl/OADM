 #include <math.h>
#include <iostream>
#include <cstdlib>


#define ACCURACY 1e-10
#define ALPHA  0.618
#define ALPHA2 0.382

double leftBorder = -1;
double rightBorder = 1;


double function(double x){
    double a = sin(2*x+1)+2;
    return 1 / (1 + exp(a));
}


/*
double function(double x){
    return sqrt(sin(exp(-2*x))+2);
}
*/


int main(){

    double x1,x2, result;
    x1 = leftBorder + (rightBorder-leftBorder)*ALPHA2;
    x2 = leftBorder + (rightBorder-leftBorder)*ALPHA;
    // x2 > x1
    int i = 0;

    while (abs(rightBorder - leftBorder) > ACCURACY){
        if(function(x1) >= function(x2)){

            leftBorder = x1;
            x1 = x2;
            x1 = leftBorder + ALPHA2*(rightBorder - leftBorder);

        }else{

            rightBorder = x2;
            x2 = x1;
            x1 = rightBorder - ALPHA2*(rightBorder - leftBorder);

        }
        i++;
    }
    

    result = function((x1+x2)/2);

    printf("x = %lf\nPerformed steps: %d\nMinimum = %lf\n",(x1+x2)/2, i, result);

    return 0;
}