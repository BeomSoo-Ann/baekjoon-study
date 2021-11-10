M = int(input())
N = int(input())

tot = 0
primeNumber_list = []


def primeNumber(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for i in range(M, N + 1):
    if primeNumber(i):
        tot += i
        primeNumber_list.append(i)

if tot == 0:
    print(-1)
else:
    print(tot)
    print(primeNumber_list[0])
