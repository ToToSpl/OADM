import numpy as np
import pandas as pd

#program written by Jacek Grzybowski and Rafal Fiedosiuk

input_table = np.matrix([
    [-3, 8],
    [7, -4]
])

def is_base_variable(sim_col):
    zeroes = 0
    for element in sim_col:
        if element == 0:
            zeroes += 1
        elif element != 1:
            return False
    return zeroes == sim_col.shape[0] - 1

def solve_simplex_table(simplex_table):

    cb = np.zeros((simplex_table.shape[0]-1, 1))
    #while True:    
    for i in range(4):
        optimality_coefficients = []
        [optimality_coefficients.append(simplex_table[:-1, i].transpose().dot(cb).var()) for i in range(simplex_table.shape[1] - 1)]

        last_row_sorted = list(range(simplex_table.shape[1] - 1))
        last_row_sorted.sort(key=lambda var : simplex_table[-1, var] - optimality_coefficients[var], reverse=True) 
        print(simplex_table[-1, :-1] - optimality_coefficients)
        if max((simplex_table[-1, :-1] - np.asmatrix(optimality_coefficients)).tolist()[0]) <= 0:
            print("Parameter u has been minimized. Break condition fulfilled.")
            break

        counter = 0
        col = 0
        ratios = {}

        while ratios == {}:
            col = last_row_sorted[counter]
            
            ratios = {str(i): simplex_table[i, -1] / simplex_table[i, col] for i in range(simplex_table.shape[0] - 1) if simplex_table[i, col] > 0}
            counter += 1

        row = int(min(ratios, key=ratios.get))
        cb[row] = simplex_table[-1, col]
        
        new_simplex_table = np.zeros(simplex_table.shape)
        new_simplex_table[-1, :] = simplex_table[-1, :]
        
        new_simplex_table[row, :] = simplex_table[row, :] / simplex_table[row, col]
 
        for i in range(simplex_table.shape[0] - 1):
            if i == row:
                continue
 
            new_simplex_table[i, :] = simplex_table[i, :] - new_simplex_table[row, :] * simplex_table[i, col]

        simplex_table = new_simplex_table
        
        print(f"Pivot element: {row}, {col}\n")
        print(pd.DataFrame(simplex_table))
    
    x_solved = []
    for i in range(simplex_table.shape[1]-1):
        if is_base_variable(simplex_table[:-1,i]):
            j = 0
            while simplex_table[j, i] != 1:
                j += 1
            x_solved.append(simplex_table[j, -1])
        else:
            x_solved.append(0.0)
    return x_solved

if __name__ == '__main__':

    #generating simplex tableu for y's

    simplex_table = np.matrix([
        [-1, 10, 1, 0, 0, 3],
        [ 1, 12, 0, 1, 0, 8],
        [ 0,  1, 0, 0, 1, 1],
        [ 1,  0, 0, 0, 0, 0]
    ])

    print(pd.DataFrame(simplex_table))
    solution = solve_simplex_table(simplex_table)
    print(f"solved x matrix: {solution}\n")