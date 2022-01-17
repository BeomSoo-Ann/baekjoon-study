# 2447 별 찍기 - 10
# first code time complexity --> O(n**3)
# next code time complexity --> O(n**2)

from sys import setrecursionlimit
from sys import stdin
from os import system

system('clear')

setrecursionlimit(10**6)


def star(n):
    if n == 3:
        return ['***', '* *', '***']

    else:
        stars = star(n//3)

        pattern = []

        for s in stars:
            pattern.append(s*3)
        for s in stars:
            pattern.append(s+' '*(n//3)+s)
        for s in stars:
            pattern.append(s*3)

        return pattern


N = int(stdin.readline())

for j in star(N):
    print(''.join(j))


#########################
#########################
####### Reference #######
#########################
#########################


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


# n = int(stdin.readline().strip())
# print('\n'.join(append_star(n)))
