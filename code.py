# 2839 suger problem
# N = 5x + 3y
# 0 3 6 9 12
# 10 13 16 19 22 (x=2 y=0~4) / 20 23 26 29 32 (x=4) /
# 05 08 11 14 17 (x=1 y=0~4) / 15 18 21 24 27 (x=3) / 25 28 31 34 37 (x=5 y=0~4)
N = int(input())

odd_list = [5, 8, 1, 4, 7]
even_list = [0, 3, 6, 9, 2]

first_num = N % 10

if first_num in odd_list:
    y = odd_list.index(first_num)
    x = (N - 3*y)//5
    if x >= 0:
        print(x + y)
    else:
        print(-1)
elif first_num in even_list:
    y = even_list.index(first_num)
    x = (N - 3*y)//5
    if x >= 0:
        print(x + y)
    else:
        print(-1)
else:
    print(-1)
