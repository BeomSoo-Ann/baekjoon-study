# 11650 Sort the Locations

from sys import stdin

N = int(stdin.readline())

Loc_list = [list(map(int, stdin.readline().split())) for _ in range(N)]

sorted_list = sorted(Loc_list, key=lambda x: (x[0], x[1]))

for i in sorted_list:
    print(i[0], i[1])