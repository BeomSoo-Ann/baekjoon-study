# No.1912

from sys import stdin

N = int(stdin.readline())
num_list = list(map(int, stdin.readline().split()))


for i in range(N):
    num_list[i] = max(num_list[i], num_list[i] + num_list[i-1])

print(max(num_list))
