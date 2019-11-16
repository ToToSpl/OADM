import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

#all made for 2d input dimension

def function(vecX):
    return pow((vecX[0][0] - 2),2) + pow((vecX[1][0] + 1),2) - 0.5*vecX[0][0].item()*vecX[1][0].item()
    #return pow((vecX[0][0] - 1),2) + pow((vecX[1][0] - 0.5),2) - 0.5*vecX[0][0].item()*vecX[1][0].item()


#golden ratio implementation
#we dont know the range for alpha so we choose arbitrary large range 
def singleOpt(x, u):
    leftBoarder = -100.0
    rightBoarder = 100.0

    alpha1 = leftBoarder + (rightBoarder-leftBoarder)*(1-0.618)
    alphaVal1 = (function(x + alpha1 * u))
    alpha2 = leftBoarder + (rightBoarder-leftBoarder)*0.618
    alphaVal2 = function(x + alpha2 * u)

    while abs(alpha1 - alpha2) > 0.001:
        if alphaVal1 < alphaVal2:
            rightBoarder = alpha2
            alpha2 = alpha1
            alphaVal2 = alphaVal1
            alpha1 = leftBoarder + (rightBoarder-leftBoarder)*(1-0.618)
            alphaVal1 = function(x + alpha1 * u)
        else:
            leftBoarder = alpha1
            alpha1 = alpha2
            alphaVal1 = alphaVal2
            alpha2 = leftBoarder + (rightBoarder-leftBoarder)*(0.618)
            alphaVal2 = function(x + alpha2 * u)

    return((alpha1+alpha2)/2)


if __name__ == "__main__":

    x = np.matrix([[1.0],[3.0]])
    u = np.matrix([[1.0,0.0],[0.0,1.0]])

    pArr = [x,x,x]

    #plot stuff
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    xaxis = np.linspace(-1.0, 3.0, num=100)
    yaxis = np.linspace(-1.0, 3.0, num=100)

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

        pArr[1] = pArr[0] + singleOpt(pArr[0], u[:,0]) * u[:,0]
        pArr[2] = pArr[1] + singleOpt(pArr[1], u[:,1]) * u[:,1]

        u[:,0] = u[:,1]
        u[:,1] = pArr[2] - pArr[0]

        xTemp = pArr[0] + singleOpt(pArr[0], u[:,1]) * u[:,1]

        #adding point to graph
        xpoints.append(xTemp[0][0].item())
        ypoints.append(xTemp[1][0].item())
        zpoints.append(function(xTemp).item())

        #break condition
        if abs(np.linalg.norm(xTemp - pArr[0])) < 0.001:
            pArr[0] = xTemp
            break
        else:
            pArr[0] = xTemp
            print(pArr[0])


    #plotting points
    for i in range(len(xpoints) - 1):
        ax.plot([xpoints[i],xpoints[i+1]],[ypoints[i],ypoints[i+1]],[zpoints[i],zpoints[i+1]],color = 'r', marker = "o")

    print('\nfinal result')
    print('x vector:')
    print(pArr[0])
    print('value of the minimum:', function(pArr[0]).item())

    plt.show()