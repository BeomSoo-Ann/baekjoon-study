# 2798 Black Jack

from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().split())

CARD_LIST = list(map(int, stdin.readline().split()))
CARD_LIST.sort()


CARD_SUM_LIST = [sum(i) for i in list(combinations(CARD_LIST, 3))]


def find_closest():
    base = 0
    for i in CARD_SUM_LIST:
        if i > M:
            pass
        else:
            if i > base:
                base = i
            else:
                pass

    return base


print(find_closest())
