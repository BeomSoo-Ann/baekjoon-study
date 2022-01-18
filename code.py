# 11729 Hanoi Tower

from sys import stdin

step = []


def move_hanoi(n, start, end, temp):

    if n == 1:
        step.append([start, end])
    else:
        move_hanoi(n-1, start, temp, end)
        step.append([start, end])
        move_hanoi(n-1, temp, end, start)

    return step


N = int(stdin.readline())

move_map = move_hanoi(N, 1, 3, 2)

print(len(move_map))

for i in move_map:
    print(i[0], i[1])
