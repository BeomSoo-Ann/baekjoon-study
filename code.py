# 10989 ordering 3

from sys import stdin, stdout

N = int(stdin.readline())
case = [0] * 10001

for _ in range(N):
    case[int(stdin.readline())] += 1
    
for i in range(10001):
    for j in range(case[i]):
        stdout.write(str(i) + '\n')
        