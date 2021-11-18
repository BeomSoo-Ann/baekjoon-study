from sys import stdin


def prime_list(n):
    base = int(n ** 0.5)
    sieve = [True] * (n-1)

    for i in range(base-1):
        if sieve[i] == True:
            for j in range(2*(i+1), n-1, i+2):
                sieve[j] = False

    return [i+2 for i in range(n-1) if sieve[i] == True]


def goldbach(n):
    primes = prime_list(n)
    middle = prime_list(n//2)
    middle.reverse()

    for p in middle:
        if n - p in primes:
            return [p, n-p]


T = int(stdin.readline())

for i in range(T):
    N = int(stdin.readline())

    if N % 2 == 0:
        print(goldbach(N)[0], goldbach(N)[1])
    else:
        pass
