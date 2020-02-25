from numpy import *
#written by Jacek Grzybowski and Rafal Fiedosiuk

A = matrix([
    [-3, 2],
    [0, 1]
])

def perp(a):
    b = empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

def seg_intersect(a1,a2, b1,b2) :
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = dot( dap, db)
    num = dot( dap, dp )
    return (num / denom.astype(float))*db + b1


#checking safe strategy
i = 0
if (A[0, :].max() < A[1, :].max()):
    i = 0
else:
    i = 1

j = 0
if (A[:, 0].min() > A[:, 1].min()):
    j = 0
else:
    j = 1

if (A[i, :].max() == A[:, j].min()):
    print(f"y{i+1} = 1, z{j+1} = 1, Sm = {A[i,j]}")
else:

    #player D1
    line11a = array([0, A[0,0]])
    line11b = array([1, A[1,0]])

    line12a = array([0, A[0,1]])
    line12b = array([1, A[1,1]])

    #player D2
    line21a = array([0, A[0,0]])
    line21b = array([1, A[0,1]])

    line22a = array([0, A[1,0]])
    line22b = array([1, A[1,1]])

    #checking for D1
    print("D1:")
    print(seg_intersect(line12a, line12b, line11a, line11b)[0])
    print(1-seg_intersect(line12a, line12b, line11a, line11b)[0])

    print("D2:")
    print(seg_intersect(line22a, line22b, line21a, line21b)[0])
    print(1-seg_intersect(line12a, line12b, line11a, line11b)[0])

    print(1-seg_intersect(line12a, line12b, line11a, line11b)[1])


