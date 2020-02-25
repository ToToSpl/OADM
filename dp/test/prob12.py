#problem no12
import numpy as np

table = np.matrix([
    [0, 5,  9, 12, 14, 15, 18, 20, 24, 27, 30, 34, 38],
    [0, 7,  9, 11, 13, 16, 19, 21, 22, 25, 28, 35, 40],
    [0, 6, 10, 13, 15, 16, 18, 21, 22, 25, 26, 29, 33]
])

def dp(i, sumU, tab, dec):
    if i == 2:
        dec[i] = 12 - sumU
        return tab[i, 12 - sumU]
    else:
        ans = [dp(i + 1, sumU + k, tab, dec) + tab[i, k] for k in range(0, 13-sumU)]
        dec[i] = np.argmax(ans)
        return max(ans)
    

if __name__ == "__main__":
    decisions = [None] * 3
    answer = dp(0, 0, table, decisions)
    dp(1, decisions[0], table, decisions)
    dp(2, decisions[0] + decisions[1], table, decisions)
    print(answer, decisions)