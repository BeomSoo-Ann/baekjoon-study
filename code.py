# 1002

from sys import stdin, exit

T = int(stdin.readline())

for i in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, stdin.readline().split())

    t = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5

    if t != 0:
        if float(t) < float(r_1 + r_2):
            print(2)
        elif float(t) == float(r_1 + r_2):
            print(1)
        else:
            print(0)
    elif t == 0:
        if r_1 == r_2:
            print(-1)
        elif r_1 != r_2:
            print(0)
    else:
        exit()
