# 10989 ordering 3

from sys import stdin, stdout

N = int(stdin.readline())
num_list = [int(stdin.readline()) for _ in range(N)]

maxi = max(num_list)

case = [0] * (maxi + 1)

for num in num_list:
    case[num] += 1
    
for i in range(maxi + 1):
    for j in range(case[i]):
        stdout.write(str(i) + '\n')

