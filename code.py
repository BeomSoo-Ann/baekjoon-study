# 10250 hotel problem
# H : 층수, W : 층 별 방 갯수, N : 손님 번호

import sys

N = int(input())

for i in range(N):
    H, W, N = map(int, sys.stdin.readline().split())

    if H == 1:
        floor_num = 1
        room_num = N

    elif W == 1:
        floor_num = N
        room_num = 1

    elif H != 1 and W != 1:
        floor_num = N % H
        room_num = N//H + 1

        if floor_num == 0:
            floor_num = H
            room_num -= 1
        else:
            pass

    else:
        pass

    print(floor_num*100 + room_num)
