# 1011 Interstellar
# 3 steps --> 1-1-1 3/0
# 4 steps --> 1-2-1 3/1
# 5 steps --> 1-2-1-1 4/1
# 6 steps --> 1-2-2-1 4/2
# 7 steps --> 1-2-1-2-1 5/2/0
# 8 steps --> 1-2-2-2-1 5/3/0
# 9 steps --> 1-2-3-2-1 5/3/1
# 10 steps --> 1-2-2-2-2-1 6/4/0
# 11 steps --> 1-2-3-2-2-1 6/4/1
# steps --> 3/1 < 4/2 < 5/3/1 < 6/4/2 < 7/5/3/1
# like a pyramid


import sys

start_point = 1

T = int(input())

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    steps = y - x

    print()
