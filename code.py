# No.14888 plus minus multiply divide

from sys import stdin


N = int(stdin.readline())
#teamstate_list = [list(map(int, stdin.readline().split())) for _ in range(N)]
# print(teamstate_list)
L = []
L_list = []


def backtrace():
    global L
    if len(L) == N//2:
        print(L)
        return

    for i in range(N):
        if i+1 in L:
            continue
        L.append(i+1)

        if len(L) != 1:
            if L[-1] < L[-2]:
                L.pop()
                continue

        backtrace()
        L_list.append(L)
        L.pop()


backtrace()
print(L_list)
