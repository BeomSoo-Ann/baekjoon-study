import sys


def primeNumber(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


N = int(input())

num_list = list(map(int, sys.stdin.readline().split()))
tot = 0

for i in range(N):
    num = num_list[i]

    if primeNumber(num) == True:
        tot += 1
    else:
        pass

print(tot)
