# No.9663 N-Queen

from sys import stdin

N = int(stdin.readline())
L = [[i for i in range(1, N+1)] for _ in range(N)]


def backtrack_queen():
    if len(L) == N:
        return

    for _ in range(N):
        L.append()
        backtrack_queen()
        L.pop()
