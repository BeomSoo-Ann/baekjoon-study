# No.1149 RGB street

from sys import stdin


N = int(stdin.readline())
base = [None] * N

for i in range(N):
    RGB_list = list(map(int, stdin.readline().split()))
    base[i] = RGB_list

L = []
sum_list = []


def make_index():
    global L
    if len(L) == N:
        # sum_list.append(make_sum(L))
        print(L)
        return

    for i in range(3):
        L.append(i)
        if len(L) != 1:
            if L[-1] == L[-2]:
                L.pop()
                continue

        make_index()
        L.pop()


def make_sum(list):
    n = 0
    tot = 0
    for i in list:
        tot += base[n][i]
        n += 1
    return tot


make_index()
print(min(sum_list))
