# No.9663 N-Queen

from sys import stdin

N = int(stdin.readline())
L = []
cnt = 0


def check_available(x):
    x_index = L.index(x)

    for i in range(x_index):
        if abs(i-x_index) == abs(L[i]-x):
            return True


def backtrack_queen():
    global cnt

    if len(L) == N:
        cnt += 1
        return

    for loc in range(N):
        if loc in L:
            continue

        L.append(loc)

        if check_available(loc):
            L.pop()
            continue

        backtrack_queen()
        L.pop()


backtrack_queen()
print(cnt)
