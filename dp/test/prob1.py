import numpy as np 
import math

look_up = np.matrix([
    [0, 3, 8, 15, 30, 40, 49, 55, 58, 60, 62, 64, 65],
    [0, None, 22, None, 32, None, 35, None, 50, None, 70, None, 90]
])

mon_cost = [150, 50, 100, 100]

def cost(k, prevVal, prevU):
    if int((prevVal + 0.5 * prevU) / 25) > 12:
        return math.inf
    else:
        return look_up[1, int(k / 25)] + look_up[0, int((prevVal + 0.5 * prevU) / 25)]

def dp(prevVal, prevU, endVal, i, decisions):
    if i == 3:
        if mon_cost[3] - prevVal >= endVal:
            decisions[3] = mon_cost[3] - prevVal
            return look_up[1, int((mon_cost[3] - prevVal) / 25)] + look_up[0, int((prevVal + 0.5 * prevU) / 25)]
        else:
            return math.inf
    beginC = max((0, mon_cost[i] - prevVal))
    ans = [dp(prevVal + k - mon_cost[i], k, endVal, i + 1, decisions) + cost(k, prevVal, prevU) for k in range(beginC, 350, 50)]
    decisions[i] = np.argmin(ans) * 50 + beginC
    return min(ans)

if __name__ == '__main__':
    dec = [None] * 4
    answer = dp(100, 0, 0, 0, dec)
    dp(100 - mon_cost[0] + dec[0], dec[0], 0, 1, dec)
    dp(100 - mon_cost[0] + dec[0] - mon_cost[1] + dec[1], dec[1], 0, 2, dec)
    dp(100 - mon_cost[0] + dec[0] - mon_cost[1] + dec[1] - mon_cost[2] + dec[2], dec[2], 0, 3, dec)
    print(answer, dec)