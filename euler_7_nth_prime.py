# https://projecteuler.net/problem=7

import math

def sieve(xmax):
    p = {i for i in range(2, xmax + 1)}
    for i in range(2, xmax):
        r = {j * i for j in range(2, int(xmax / i) + 1)}
        p -= r
    return sorted(p)

print(sum(sieve(2000000)))
