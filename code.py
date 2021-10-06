# 1011 Interstellar
# 1 step --> 1
# 2 steps --> 1-1 2 `2`
# 3 steps --> 1-2-1 3/1 `4`
# 4 steps --> 1-2-2-1 4/2 `6`
# 5 steps --> 1-2-3-2-1 5/3/1 `9`
# 6 steps --> 1-2-3-3-2-1 6/4/2 `12`
# 7 steps --> 1-2-3-4-3-2-1 7/5/3/1 `16`
# 8 steps --> 1-2-3-4-4-3-2-1 8/6/4/2 `20`
# 9 steps --> 1-2-3-4-5-4-3-2-1 9/7/5/3/1 `25`
# like a pyramid

import sys

T = int(input())

# found logic but no idea to create code

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    steps = y - x

    print()
