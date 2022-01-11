# 2447 별 찍기 - 10
# first code time complexity --> O(n**2)

from sys import stdin
from os import system

system('clear')


def star(n):
    if n == 3:
        return ['***', '* *', '***']
    else:
        pattern_1 = [star(n//3)[i] * 3 for i in range(n//3)]
        pattern_2 = [star(n//3)[i] + ' ' * (n//3) + star(n//3)[i]
                     for i in range(n//3)]
        return pattern_1 + pattern_2 + pattern_1


N = int(stdin.readline())

print(star(N))

for j in range(N):
    print(''.join(star(N)[j]))
