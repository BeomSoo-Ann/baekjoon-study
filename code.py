# Goldbach conjecture
from sys import stdin


def primeNumber(N):
    prime = True
    prime_list = [prime] * N

    for i in range(2, N):
        if prime_list[i] == True:
            for j in range(i*i, N, i):
                prime_list[j] = False

    first_half = [i for i in range(2, N//2+1) if prime_list[i] == True]
    second_half = [i for i in range(N//2, N) if prime_list[i] == True]

    first_half.reverse()

    return first_half, second_half


def goldbach(N):
    first_half, second_half = primeNumber(N)

    for i in first_half:
        for j in second_half:
            if i + j == N:
                print(i, j)
                return


T = int(input())

for i in range(T):
    N = int(stdin.readline())
    if N % 2 == 0:
        goldbach(N)
    else:
        pass


# PLUS ALPHA


# limited_num=10000
# eratos = [False,False]+[True]*~-limited_num
# for i in range(2,int(limited_num**.5)+1):eratos[2*i::i]=[False]*(limited_num//i-1)
#
# n = int(input())
# T = [ int(input()) for _ in range(n) ]
# for i in T:
#     for j in range(i//2,i+1):
#         if eratos[j] and eratos[i-j]:print(i-j,j);break
