# 2447 별 찍기 - 10
# first code time complexity --> O(n**3)
# next code time complexity --> O(n**2)

from sys import setrecursionlimit
from sys import stdin
from os import system

system('clear')


def star(n):
    if n == 3:
        return ['***', '* *', '***']

    else:
        star(n//3)

        pattern_1 = []
        pattern_2 = []

        for i in range(n//3):
            pattern_1.append(star(n//3)[i] * 3)
            pattern_2.append(star(n//3)[i] + ' ' * (n//3) + star(n//3)[i])

        return pattern_1 + pattern_2 + pattern_1


# N = int(stdin.readline())
#
# for j in star(N):
#     print(''.join(j))
#
###################################################################################


setrecursionlimit(10**6)


def append_star(LEN):
    if LEN == 1:
        return ['*']

    STAR = append_star(LEN//3)
    L = []

    for S in STAR:
        L.append(S*3)
    for S in STAR:
        L.append(S+' '*(LEN//3)+S)
    for S in STAR:
        L.append(S*3)

    return L


n = int(stdin.readline().strip())
print('\n'.join(append_star(n)))
