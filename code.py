# 2750 order

from sys import stdin


N = int(stdin.readline())

NUM_list = [int(stdin.readline()) for _ in range(N)]
NUM_list.sort()

for i in range(N):
    print(NUM_list[i])
