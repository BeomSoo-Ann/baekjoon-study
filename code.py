# No.1904 tile

from sys import stdin
from math import factorial


N = int(stdin.readline())
dub_zero = N//2


def make_tile(n):
    if n == 0:
        return 1

    if n == 1:
        return N-1

    if N % 2 == 0:
        if n == dub_zero:
            return 1

    if N % 2 == 1:
        if n == dub_zero:
            return dub_zero+1

    num = factorial(N-n) // (factorial(n)*factorial(N-n-n))
    return num


tot = 0

for i in range(dub_zero+1):
    tot += make_tile(i)

print(tot % 15746)
