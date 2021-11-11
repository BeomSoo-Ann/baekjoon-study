import sys


M, N = map(int, sys.stdin.readline().split())


def prime_list(m, n):
    if m == n and m > 1:
        print((m))

    sieve = [True] * n

    base = int(n ** 0.5)

    for i in range(2, base + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    base_list = [i for i in range(2, n) if sieve[i] == True]

    for i in range(len(base_list)):
        if base_list[i] >= m:
            print(base_list[i])


prime_list(M, N)
