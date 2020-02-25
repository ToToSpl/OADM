import numpy as np
import pandas as pd

#program written by Jacek Grzybowski and Rafal Fiedosiuk

''' ax^2 + by^2 + cxy + dx + ey '''
function_coefficients = np.matrix([[0, 2, 0, 3, -5]])

inequalitiesLHS = np.matrix([[5, 3, 1, 0],
                            [2, 3, 0, 1]])

inequalitiesRHS = np.matrix([[7, 4]])

#this function creates first simplex tableux
def qpToLp(function_coefficients, inequalitiesLHS, inequalitiesRHS):
    D = np.zeros((4, 4))
    D[0, 0] = function_coefficients[0, 0]
    D[1, 1] = function_coefficients[0, 1]
    D[0, 1] = function_coefficients[0, 2] / 2
    D[1, 0] = function_coefficients[0, 2] / 2
    Q = 2 * D

    b = inequalitiesRHS.transpose()

    A = inequalitiesLHS

    c = np.zeros((4, 1))
    c[0, 0] = function_coefficients[0, 3]
    c[1, 0] = function_coefficients[0, 4]

    delta = np.zeros((4, 4))
    Qb = D[:, 2:4]
    
    for i, value in enumerate(c[:, 0]):
        if -value - Qb[i, :] * b < 0:
            delta[i, i] = -1
        else:
            delta[i, i] = 1
    
    #writing smaller matricies into the big one 
    table = np.zeros((6, 17))
    table[0:2, 0:4] = A
    table[2:6, 0:4] = Q
    table[2:6, 4:6] = A.transpose()
    table[2:6, 6:8] = -A.transpose()
    table[2:6, 8:12] = -np.identity(4)
    table[2:6, 12:16] = delta
    table[0:2, 16:17] = b
    table[2:6, 16:17] = -c

    #if c is negative the given row is multiplied by -1
    for i in range(table.shape[0] - b.shape[0]):
        if table[b.shape[0] + i, -1] < 0:
            table[b.shape[0] + i, :] = -table[b.shape[0] + i, :] 
    
    return table

#function for checking if the given row is a base
def is_base_variable(sim_col):
    zeroes = 0
    for element in sim_col:
        if element == 0:
            zeroes += 1
        elif element != 1:
            return False
    return zeroes == sim_col.shape[0] - 1

#checks for given mu or x if corresponding x or mu is in the base
def check_constrain(sim_tab, i):
    if i <= 3:
        return not is_base_variable(sim_tab[:, i + 8])
    elif i >= 8 and i >= 11:
        return not is_base_variable(sim_tab[:, i - 8])
    else:
        return True

#main part of the algorithm
def solve_simplex_table(simplex_table):
    col = 0
    sum_u = np.zeros(simplex_table.shape[1]-1)
    sum_u[12:16] = np.ones(4)
    cb = [0.0, 0.0, 1.0, 1.0, 1.0, 1.0]

    while True:    
        optimality_coefficients = []
        [optimality_coefficients.append(simplex_table[:, i].transpose().dot(cb)) for i in range(simplex_table.shape[1] - 1)]
        #print(optimality_coefficients)
        last_row_sorted = list(range(simplex_table.shape[1] - 1))
        last_row_sorted.sort(key=lambda var : sum_u[var] - optimality_coefficients[var], reverse=False) 

        #break condition fulfilled if the smallest element in the optimality row is non-negative aka there are no negative numbers
        if min((sum_u - optimality_coefficients)[0:4]) >= 0:
            print("Parameter u has been minimized. Break condition fulfilled.")
            break

        counter = 0
        ratios = {}

        #if the smallest number cant be set as a pivot the next smallest number will be choosen
        while ratios == {}:
            col = last_row_sorted[counter]
            
            ratios = {str(i): simplex_table[i, -1] / simplex_table[i, col] for i in range(simplex_table.shape[0] - 1) if simplex_table[i, col] > 0 and check_constrain(simplex_table, col)}
            counter += 1

        #ratios of the y axis of the pivot. Choosed by the smallest non-negative
        row = int(min(ratios, key=ratios.get))

        cb[row] = sum_u[col]
        
        new_simplex_table = np.zeros(simplex_table.shape)

        #algorithm for calculating next simplex tableux according to Prof. Smieja lecture of LP
        for m in range(simplex_table.shape[0]):
            if m == row:
                new_simplex_table[row, :] = simplex_table[row, :] / simplex_table[row, col]
                continue
            for n in range(simplex_table.shape[1]):
                if n == col:
                    continue
                new_simplex_table[m, n] = simplex_table[m, n] - (simplex_table[m, col] * simplex_table[row, n]) / simplex_table[row, col]

        simplex_table = new_simplex_table

        print(f"Pivot element: {row}, {col}\n")
        
        print(pd.DataFrame(simplex_table))
    
    x_solved = []
    for i in range(4):
        if is_base_variable(simplex_table[:,i]):
            j = 0
            while simplex_table[j, i] != 1:
                j += 1
            x_solved.append(simplex_table[j, -1])
        else:
            x_solved.append(0.0)
    return x_solved



if __name__ == '__main__':

    simplex_table = qpToLp(function_coefficients, inequalitiesLHS, inequalitiesRHS)
    #simplex_table = qpToLp(np.matrix([[1,1,0,-2,-2]]), np.matrix([[1,2,1,0],[2,3,0,1]]), np.matrix([[8, 2]]))

    print('First simplex tableux:')
    print(pd.DataFrame(simplex_table))
    solution = solve_simplex_table(simplex_table)
    print(f"solved x matrix: {solution}\n")