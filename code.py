#2751 order

from sys import stdin

N = int(stdin.readline())
NUM_list = [int(stdin.readline()) for _ in range(N)]

#################### 2750 solution ####################

# NUM_list.sort()
# 
# for i in range(N):
#     print(NUM_list[i])

#################### use .sorted() ####################

for i in sorted(NUM_list):
    print(i)

# result: 8ms faster, similar to 2750
