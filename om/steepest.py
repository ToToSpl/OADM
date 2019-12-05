#CREATED BY JACEK GRZYBOWSKI AND RAFAŁ FIEDOSIUK

import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

#all made for 2d input dimension

def function(vecX):
    return pow((vecX[0][0] - 2),2) + pow((vecX[1][0] + 1),2) - 0.5*vecX[0][0].item()*vecX[1][0].item()
    #return pow((vecX[0][0] - 1),2) + pow((vecX[1][0] - 0.5),2) - 0.5*vecX[0][0].item()*vecX[1][0].item()

def gradient(vecX):
    return np.matrix([[(2*vecX[1][0]-0.5*vecX[0][0]+2).item()],[(2*vecX[0][0]-0.5*vecX[1][0]-4).item()]])
    #return np.matrix([[(2*vecX[1][0]-0.5*vecX[0][0]-2).item()],[(2*vecX[0][0]-0.5*vecX[1][0]-1).item()]])

#golden ratio implementation
#we dont know the range for alpha so we choose arbitrary large range 
def singleOpt(x, u):
    leftBorder = -100.0
    rightBorder = 100.0

    alpha1 = leftBorder + (rightBorder-leftBorder)*(1-0.618)
    alphaVal1 = (function(x - alpha1 * u))
    alpha2 = leftBorder + (rightBorder-leftBorder)*0.618
    alphaVal2 = function(x - alpha2 * u)

    while abs(alpha1 - alpha2) > 0.001:
        if alphaVal1 < alphaVal2:
            rightBorder = alpha2
            alpha2 = alpha1
            alphaVal2 = alphaVal1
            alpha1 = leftBorder + (rightBorder-leftBorder)*(1-0.618)
            alphaVal1 = function(x - alpha1 * u)
        else:
            leftBorder = alpha1
            alpha1 = alpha2
            alphaVal1 = alphaVal2
            alpha2 = leftBorder + (rightBorder-leftBorder)*(0.618)
            alphaVal2 = function(x - alpha2 * u)

    return (alpha1+alpha2)/2



if __name__ == "__main__":

    x = np.matrix([[1.0],[3.0]])

    #function plot stuff
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    xaxis = np.linspace(-1.0, 3.5, num=100)
    yaxis = np.linspace(-1.0, 3.5, num=100)

    xaxis,yaxis = np.meshgrid(xaxis,yaxis)

    zaxis = pow(xaxis-2,2) + pow(yaxis+1,2) - 0.5*xaxis*yaxis
    #zaxis = pow(xaxis-1,2) + pow(yaxis-0.5,2) - 0.5*xaxis*yaxis
    ax.plot_wireframe(xaxis, yaxis, zaxis, rcount = 10, ccount = 10)

    xpoints = []
    ypoints = []
    zpoints = []

    xpoints.append(x[0][0].item())
    ypoints.append(x[1][0].item())
    zpoints.append(function(x).item())
    #end of plotting stuff

    for i in range(100):
        tempX = x - singleOpt(x,gradient(x))*gradient(x)

        xpoints.append(tempX[0][0].item())
        ypoints.append(tempX[1][0].item())
        zpoints.append(function(tempX).item())
        print(tempX)

        #break condition
        if abs(np.linalg.norm(tempX - x)) < 0.001:
            x = tempX
            break
        else:
            x = tempX


    #plotting points
    for i in range(len(xpoints) - 1):
        ax.plot([xpoints[i],xpoints[i+1]],[ypoints[i],ypoints[i+1]],[zpoints[i],zpoints[i+1]],color = 'r', marker = "o")

    print('\nfinal result')
    print('x vector:')
    print(x)
    print('value of the minimum:', function(x).item())

    plt.show()