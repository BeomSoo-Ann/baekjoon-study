# 10989 ordering 3

from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10**7)

N = int(stdin.readline())
num_list = [int(stdin.readline()) for _ in range(N)]


L = len(num_list)
maxi = max(num_list)


count_base = []

for i in range(L):
    order = num_list.count(i)
    count_base.append(order)


count_sum = []
count_sum.append(count_base[0])

for i in range(1, maxi + 1):
    count_sum.append(count_sum[i - 1] + count_base[i])


list_sorted = [0] * (L+1)
    
for i in range(L-1, -1, -1):
    list_sorted[count_sum[num_list[i]]] = num_list[i]
    count_sum[num_list[i]] -= 1


for i in list_sorted[1:]:
    stdout.write(str(i) + '\n')