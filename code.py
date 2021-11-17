import sys


def prime_list(n):

    sieve = [True] * (n+1)

    base = int(n ** 0.5)

    for i in range(2, base + 1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return [i for i in range(2, n+1) if sieve[i] == True]


while True:
    N = int(input())
    tot = 0

    if N == 0:
        sys.exit()

    for i in prime_list(2*N):
        if i > N:
            tot += 1

    print(tot)
