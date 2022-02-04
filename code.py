# No.18870 narrow down the location

from sys import stdin


N = int(stdin.readline())
loc_list = list(map(int, stdin.readline().split()))
sorted_list = sorted(set(loc_list))

loc_dict = {}
order = 0

for i in sorted_list:
    loc_dict[i] = order
    order += 1


for i in loc_list:
    print(loc_dict[i], end=' ')
