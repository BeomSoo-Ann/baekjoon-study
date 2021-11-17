def prime_list(n):

    sieve = [True] * (n+1)

    base = int(n ** 0.5)

    for i in range(2, base + 1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return [i for i in range(2, n+1) if sieve[i] == True]


def goldbach(n):
    primes = prime_list(n)
    partitions = []

    for p in primes:
        if n - p in primes:
            if p > n-p:
                pass
            else:
                partitions.append([p, n - p])

    return partitions


T = int(input())

for i in range(T):

    N = int(input())

    if N % 2 == 0:
        print(goldbach(N)[-1][0], goldbach(N)[-1][1])
    else:
        break
