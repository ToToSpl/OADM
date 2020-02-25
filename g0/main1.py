from scipy.optimize import linprog
import numpy as np


A = np.matrix([
    [5, -10, 0, 4, -7],
    [-3, 12, -1, -10, 6],
    [-2, 0, 4, 4, -3],
    [4, -8, -5, -4, 1],
    [-7, 9, 3, 6, -12]])
D1 = np.zeros((A.shape[0], A.shape[1]+1))

D1[:, 0:A.shape[1]] = A
D1[:, -1] = -1

D2 = np.zeros((A.shape[1], A.shape[0]+1))
D2[:, 0:A.shape[1]] = A.transpose()
D2[:, -1] = -1
D2 = -D2

c1 = [0, 0, 0, 0, 0, 1]
c2 = [0, 0, 0, 0, 0, -1]
b_in = [0, 0, 0, 0, 0]
A_eq = [[1, 1, 1, 1, 1, 0]]
b_eq = [1]
y_bounds = (0, 1)
Sm_bounds = (None, None)

'''
A = np.matrix([
    [12, 6],
    [3, 18]
    ])
D1 = np.zeros((A.shape[0], A.shape[1]+1))

D1[:, 0:A.shape[1]] = A
D1[:, -1] = -1

D2 = np.zeros((A.shape[1], A.shape[0]+1))
D2[:, 0:A.shape[1]] = A.transpose()
D2[:, -1] = -1
D2 = -D2

c1 = [0, 0 , 1]
c2 = [0, 0, -1]
b_in = [0, 0]
A_eq = [[1, 1, 0]]
b_eq = [1]
y_bounds = (0, 1)
Sm_bounds = (None, None)
'''

#finding D1
print("Player D1:\n")
res = linprog(c2, A_ub=D2, b_ub=b_in, A_eq=A_eq, b_eq=b_eq, bounds=[y_bounds, y_bounds, y_bounds, y_bounds, y_bounds, Sm_bounds])
print(f"y1 = {res['x'][0]}, y2 = {res['x'][1]}, y3 = {res['x'][2]}, y4 = {res['x'][3]}, y5 = {res['x'][4]}")

print("\n")

#finding D2
print("Player D1:\n")
res = linprog(c1, A_ub=D1, b_ub=b_in, A_eq=A_eq, b_eq=b_eq, bounds=[y_bounds, y_bounds, y_bounds, y_bounds, y_bounds, Sm_bounds])
print(f"z1 = {res['x'][0]}, z2 = {res['x'][1]}, z3 = {res['x'][2]}, z4 = {res['x'][3]}, z5 = {res['x'][4]}")


