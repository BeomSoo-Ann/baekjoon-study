# No.1003 fibonacci

from sys import stdin, stdout


T = int(stdin.readline())


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for _ in range(T):
    N = int(stdin.readline())
    if N == 0:
        print(1, 0)
        continue
    print(fibonacci(N-1), fibonacci(N))
