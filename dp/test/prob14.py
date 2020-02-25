import numpy as np

table = np.matrix([
    [0, 17, 38, 50, 55, 60],
    [0, 25, 40, 48, 56, 62],
    [0, 20, 35, 52, 60, 68],
    [0, 30, 45, 50, 55, 68]
])

def dp(i, prevU, dec):
    if i == 3:
        dec[i] = 50 if prevU == 0 else 300 - prevU
        return table[i, int(dec[i] / 50)]
    else:
        ans = [dp(i + 1, prevU + k, dec) + table[i, int(k / 50)] for k in range(0, 300 - prevU, 50)]
        dec[i] = np.argmax(ans) * 50
        return max(ans)

if __name__ == "__main__":
    dec = 4 * [None]
    val = dp(0, 0, dec)
    dp(1, dec[0], dec)
    dp(2, dec[0] + dec[1], dec)
    dp(3, dec[0] + dec[1] + dec[2], dec)
    print(val, dec)
    
    