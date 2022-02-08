# No.15649

from sys import stdin

N, M = map(int, stdin.readline().split())
L = []


def backtracking_num():
    if len(L) == M:
        print(' '.join(map(str, L)))
        return

    for i in range(1, N+1):
        if i in L:
            continue

        L.append(i)

        if len(L) != 1:
            if L[-1] < L[-2]:
                L.pop()
                continue

        backtracking_num()
        L.pop()


backtracking_num()
