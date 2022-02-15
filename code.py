# No.1003 fibonacci

from sys import stdin, stdout


T = int(stdin.readline())


<<<<<<< Updated upstream
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
=======
zero = [1, 0, 1]
one = [0, 1, 1]


def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[num], one[num]))


for _ in range(T):
    fibonacci(int(stdin.readline()))
>>>>>>> Stashed changes
