# No.1085 Out of Square

from sys import stdin

x, y, w, h = map(int, stdin.readline().split())

dist_list = [x, y, w-x, h-y]
print(min(dist_list))
