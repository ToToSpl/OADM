% written by Jacek Grzybowski and Rafal Fiedosiuk

Q = [0 0 0 0; 0 4 0 0; 0 0 0 0; 0 0 0 0];
c = [3; -5; 0; 0];
A = [5 3 1 0; 2 3 0 1];
b = [7; 4];
x = quadprog(Q, c, A, b, [], [], 0, [])
 
value = 3*x(1)^2 - 5*x(2) + 2 * x(2)^2