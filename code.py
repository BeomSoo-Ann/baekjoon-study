# 3053

from sys import stdin
from math import pi

r = int(stdin.readline())

u_circle = pi * r * r
t_circle = float(2 * r * r)

print("{:.6f}".format(u_circle))
print("{:.6f}".format(t_circle))
