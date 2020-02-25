import numpy as np 

table = np.matrix([
    [10, 18, 8, 11, 12],
    [15, 13, 10, 7, 9]
])

storage = [14, 10, 15, 9, 12]

END = 4

def returnVal(i, k):
    if k > 0:
        return k * -table[0, i]
    elif k < 0:
        return k * table[1, i]
    else:
        return 0

def dp(i, prevVal, endVal, dec):
    if i == END:
        dec[i] = endVal - prevVal
        return returnVal(i, endVal - prevVal)
    else:
        ans = [dp(i + 1, prevVal + k, endVal, dec) + returnVal(i, k) for k in range(-prevVal, storage[i + 1] - prevVal + 1)]
        dec[i] = np.argmax(ans) - prevVal
        return max(ans)

if __name__ == "__main__":
    dec = 5 * [None]
    ans = dp(0, 4, 10, dec)
    dp(1, 4+dec[0], 10, dec)
    dp(2, 4+dec[0]+dec[1], 10, dec)
    dp(3, 4+dec[0]+dec[1]+dec[2], 10, dec)
    dp(4, 4+dec[0]+dec[1]+dec[2]+dec[3], 10, dec)

    print(ans, dec)