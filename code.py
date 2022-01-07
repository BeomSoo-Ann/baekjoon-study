# 2447 별 찍기 - 10

from sys import stdin
from os import system

system('clear')


def star(n):
    pattern_1 = ['*', '*', '*']
    pattern_2 = ['*', ' ', '*']

    if n == 3:
        return pattern_1 + pattern_2 + pattern_1
    else:
        line_1 = []
        return


print(star(3))
