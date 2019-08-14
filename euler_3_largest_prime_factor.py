# https://projecteuler.net/problem=3

import math

def sieve(xmax):
    p = {i for i in range(2, xmax + 1)}
    for i in range(2, xmax):
        r = {j * i for j in range(2, int(xmax / i) + 1)}
        p -= r
    return p

input = 600851475143
# input = 13195

p = sieve(int(math.sqrt(input)) + 2)

f = {i for i in p if input % i == 0}

print(max(f))
