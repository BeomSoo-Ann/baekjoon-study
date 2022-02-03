# 1427 Sort inside

from sys import stdin

from numpy import sort

N = stdin.readline()

N_list = sorted(N, reverse=True)

print(''.join(N_list).strip())