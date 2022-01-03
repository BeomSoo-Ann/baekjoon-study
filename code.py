# 4153

from sys import stdin, exit

while True:
    len_list = list(map(int, stdin.readline().split()))

    len_list.sort()

    if len_list[2]**2 == len_list[0]**2 + len_list[1]**2 and 0 not in len_list:
        print("right")
    elif len_list[0] == 0 and len_list[1] == 0 and len_list[2] == 0:
        break
    else:
        print("wrong")
