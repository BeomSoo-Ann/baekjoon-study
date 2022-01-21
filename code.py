# 2231 분해합
# N = a//base + a//(base-1) + ... + a//1

from sys import stdin

N = int(stdin.readline())
base = len(str(N))

for i in range(1, N+1):
    SUM = sum(map(int, str(i)))
    i_sum = i + SUM

    if i_sum == N:
        print(i)
        break

    elif i == N:
        print(0)
        break

    else:
        pass
