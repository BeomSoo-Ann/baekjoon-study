import sys


M, N = map(int, sys.stdin.readline().split())


def prime_list(n):

    sieve = [True] * n

    base = int(n ** 0.5)

    for i in range(2, base + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]


def primeNumber(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


if M == N:
    if primeNumber(M):
        print(M)
elif M < N:
    for i in prime_list(N):
        if i >= M:
            print(i)
