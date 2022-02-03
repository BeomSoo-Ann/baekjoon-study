# 2108 Statistic


from sys import stdin

N = int(stdin.readline())
num_list = [int(stdin.readline()) for _ in range(N)]

maxi_list = max(num_list)
mini_list = min(num_list)

def arithmetic_mean(L, n):
    S = sum(L)
    mean_num = S / n
    print(round(mean_num))


def median(L, n):
    L.sort()
    if n % 2 == 0:
        median_num = (L[n//2] + L[n//2 - 1]) / 2
        print(median_num)
    else:
        median_num = L[n//2]
        print(median_num)
        

def find_mode(L, n):
    L.sort()
    cnt = 1
    cnt_list = [1]
    
    for i in range(1, n):
        if L[i] == L[i-1]:
            cnt += 1
            cnt_list.append(cnt)
        else:
            cnt = 1
            cnt_list.append(cnt)
    
    max_cnt = max(cnt_list)

    index_list = []
    
    for i in cnt_list:
        if i == max_cnt:
            index_list.append(cnt_list.index(i))
            cnt_list[cnt_list.index(i)] = 0
        else:
            pass
    
    if len(index_list) == len(cnt_list):
        if len(cnt_list) == 1:
            print(L[0])
        else:
            print(L[1])
    else:
        if len(index_list) == 1:
            print(L[index_list[0]])
        else:
            print(L[index_list[1]])
        
 
arithmetic_mean(num_list, N)
median(num_list, N)
find_mode(num_list, N)
print(maxi_list - mini_list)