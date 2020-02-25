import numpy as np
from numpy import unravel_index

table = np.matrix([
    [10,  5, 8, 7, 6], #p
    [10, 12, 5, 4, 8]  #u
])

NUM_OF_STEPS = 5
MAX_CARGO = 50

#p - buy
#u - sell
#dec = (p, u)

def dp(i, prevCargo, tab, dec):
    if i == NUM_OF_STEPS:
        dec[i - 1] = [0, prevCargo]
        return dec[i - 1][1] * tab[1, i - 1] - dec[i - 1][0] * tab[0, i - 1]
    else:
        vals = np.zeros((2,2))
        for u in range(2):
            for p in range(2):
                u_ = u * prevCargo
                p_ = p * (MAX_CARGO - prevCargo + u_)
                vals[p, u] = dp(i + 1, prevCargo - u_ + p_, tab, dec) + u_ * tab[1, i - 1] - p_ * tab[0, i - 1]

        dec_ = unravel_index(vals.argmax(), vals.shape)
        dec[i-1][0] = dec_[0] * prevCargo
        dec[i-1][1] = dec_[1] * (MAX_CARGO - prevCargo + dec[i-1][0])
        return np.amax(vals)


if __name__ == '__main__':
    dec = NUM_OF_STEPS * [[None, None]]
    ans = dp(1, 0, table, dec)
    print(dec)
    prevCargo = dec[0][0] - dec[0][1]
    for i in range(2, NUM_OF_STEPS + 1):
        dp(i, prevCargo, table, dec)
        print(dec)
        prevCargo += (dec[i - 1][0] - dec[i - 1][1])

    print(ans, dec)
        