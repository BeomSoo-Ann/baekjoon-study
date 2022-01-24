# 7568 덩치

from sys import stdin

N = int(stdin.readline())

PARTY = [list(map(int, stdin.readline().split())) for i in range(N)]

for HUMAN_1 in PARTY:
    ORDER = 1

    for HUMAN_2 in PARTY:
        if HUMAN_2[0] > HUMAN_1[0] and HUMAN_2[1] > HUMAN_1[1]:
            ORDER += 1
        else:
            pass

    print(ORDER, end=' ')
