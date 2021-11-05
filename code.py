# 1011 Interstellar
# 1 step --> 1
# 2 steps --> 1-1 2 `2`
# 3 steps --> 1-2-1 3/1 `3~4`
# 4 steps --> 1-2-2-1 4/2 `5~6`
# 5 steps --> 1-2-3-2-1 5/3/1 `7~9`
# 6 steps --> 1-2-3-3-2-1 6/4/2 `10~12`
# 7 steps --> 1-2-3-4-3-2-1 7/5/3/1 `13~16`
# 8 steps --> 1-2-3-4-4-3-2-1 8/6/4/2 `17~20`
# 9 steps --> 1-2-3-4-5-4-3-2-1 9/7/5/3/1 `21~25`
# like a pyramid

import sys

T = int(sys.stdin.readline())
for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    jump = y - x

    if jump < 0:
        print("error")
    elif jump == 0:
        step = 0
    elif jump == 1:
        step = 1
    elif jump == 2:
        step = 2
    elif jump >= 3:
        i = 1

        while True:
            jump -= 2*i
            checker = 2*i

            if jump > 0:
                i += 1
                if jump <= i:
                    step = 2*i - 1
                elif jump > i:
                    step = 2*i
            elif jump <= 0:
                break
            else:
                break

    print(step)
