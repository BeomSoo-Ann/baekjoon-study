# 1018 Chess coloring

from sys import stdin

M, N = map(int, stdin.readline().split())

SQUARE = [list(map(str, stdin.readline().strip())) for _ in range(M)]
BASE = []

for i in range(1, M+1):
    L = []
    for j in range(1, N+1):
        if i % 2 == 1 and j % 2 == 1:
            L.append('B')
        elif i % 2 == 1 and j % 2 == 0:
            L.append('W')
        elif i % 2 == 0 and j % 2 == 1:
            L.append('W')
        elif i % 2 == 0 and j % 2 == 0:
            L.append('B')
    BASE.append(L)

print(BASE)


def COUNT_ERROR(BOARD):
    for line in BOARD:
        for sqr in line:
            return
