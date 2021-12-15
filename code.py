# Goldbach Conjecture

def prime(n):
    sieve = [True] * n

    base = int(n ** 0.5)
    for i in range(2, base+1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i]]


print(prime(100))
