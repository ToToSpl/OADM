import numpy as np

#pastebin pastebin.com/gPhyrN2z
'''

Q = [0 0 0 0; 0 4 0 0; 0 0 0 0; 0 0 0 0];
c = [3; -5; 0; 0];
A = [5 3 1 0; 2 3 0 1];
b = [7; 4];
x = quadprog(Q, c, A, b, [], [], 0, [])
 
value = 3*x(1)^2 - 5*x(2) + 2 * x(2)^2

'''

qC = np.matrix([[0, 2, 0, 3, -5]])
inCof = np.matrix([[5, 3, 1, 0], [2, 3, 0, 1]])
riCoef = np.matrix([[7, 4]])

def qpTolp(quadCoef, inCoef, righInCoef):
    D = np.zeros((inCoef.shape[1],inCoef.shape[1]))
    D[0, 0] = quadCoef[0, 0]
    D[1, 1] = quadCoef[0, 1]
    D[0, 1] = quadCoef[0, 2]/2
    D[1, 0] = quadCoef[0, 2]/2

    c = np.zeros((4,1))
    c[0, 0] = quadCoef[0, 3]
    c[1, 0] = quadCoef[0, 4]

    A = inCoef

    b = riCoef.transpose()

    delta = np.zeros((inCoef.shape[1],inCoef.shape[1]))

    Q = 2*D

    Qb = Q[:, 2:4]
    for i, c_ in enumerate(c.transpose()[0]):
        Qi = Qb[i]
        if -c_-Qi*b >= 0:
            delta[i, i] = 1
        else:
            delta[i, i] = -1

    

    tableux = np.zeros((A.shape[0]+D.shape[0], D.shape[1]+2*A.shape[0]+8 + 1))
    
    tableux[0:2, 0:4] = A
    tableux[2:6, 0:4] = Q
    tableux[2:6, 4:6] = A.transpose()
    tableux[2:6, 6:8] = -A.transpose()
    tableux[2:6, 8:12] = -np.identity(4)
    tableux[2:6, 12:16] = delta



    tableux[0:2, 16:17] = b
    rev = -c
    for i, c_ in enumerate(c.transpose()[0]):
        tableux[2+i, 16] = -c_
        if (c_ > 0):
            tableux[2+i, :] = -tableux[2+i, :]
    #tableux[2:6, 16:17] = -c
    #print(tableux)
    return tableux

    
def simplex(tableux):
    row = 0
    for i, c in enumerate(tableux[5, :]):
        if c > tableux[5, row]:
            row = i

    col = 0
    a = tableux[-1:,row]
    for i in range(a.shape[0]):
        if a[i] <= 0:
            continue

        if tableux[col, 16]/a[col] > tableux[i, 16]/a[i]:
            col = i

    print(col, row)
            
    
    


if __name__ == '__main__':
    tab = qpTolp(qC, inCof, riCoef)
    print(tab)
    simplex(tab)