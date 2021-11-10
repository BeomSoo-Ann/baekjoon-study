# 소인수분해
import sys

N = sys.stdin.readline()
i = 2

if N == 1:
    sys.exit()


while True:
    if N % i == 0 and N != i:
        print(i)
        N //= i
        continue
    elif N % i != 0:
        i += 1
        continue
    elif i == N:
        print(N)
        break
