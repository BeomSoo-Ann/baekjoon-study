# No.3009

from sys import stdin

x = list(map(int, stdin.readline().split()))
y = list(map(int, stdin.readline().split()))
z = list(map(int, stdin.readline().split()))

loc_x = [x[0], y[0], z[0]]
loc_y = [x[1], y[1], z[1]]

loc_x.sort()
loc_y.sort()

if loc_x.count(loc_x[0]) == 1:
    w_x = loc_x[0]
else:
    w_x = loc_x[2]

if loc_y.count(loc_y[0]) == 1:
    w_y = loc_y[0]
else:
    w_y = loc_y[2]

print(w_x, w_y)
