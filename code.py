# No.9461 triangle

from sys import stdin


base = [0] * 100

base[0] = 1
base[1] = 1
base[2] = 1
base[3] = 2
base[4] = 2
base[5] = 3
base[6] = 4
base[7] = 5
base[8] = 7
base[9] = 9

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())

    if N <= 10:
        print(base[N-1])
        continue

    for i in range(10, N):
        base[i] = base[i-1] + base[i-5]
    print(base[N-1])
