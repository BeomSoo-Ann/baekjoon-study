# Goldbach conjecture

def primeNumber(N):
    prime = True
    prime_list = [prime] * N

    for i in range(2, N):
        if prime_list[i] == True:
            for j in range(i*i, N, i):
                prime_list[j] = False

    return [i for i in range(2, N) if prime_list[i] == True]


print(primeNumber(100))
