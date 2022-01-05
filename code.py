# 10872

from sys import stdin


def pactorial(n):
    if n == 0:
        return 1
    else:
        return n * pactorial(n-1)


N = int(stdin.readline())

print(pactorial(N))
