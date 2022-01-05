# 1002

from sys import stdin

T = int(stdin.readline())

for i in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, stdin.readline().split())

    t = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5

    r = float(r_1 + r_2)
    r_list = [r_1, r_2]

    if t == 0:
        if r_1 == r_2:
            print(-1)
        else:
            print(0)

    elif t != 0:
        if r < t:
            print(0)
        elif r == t:
            print(1)
        else:
            if abs(r_1 - r_2) == t:
                print(1)
            elif max(r_list) > t + min(r_list):
                print(0)
            else:
                print(2)
    else:
        pass
