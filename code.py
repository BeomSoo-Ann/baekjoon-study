# 2775 APT problem
# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
# floor : n >= 1  room : k <= 14
# ground floor --> 1 2 3 4 ... 14
# first floor --> 1 3 6 10 ... 105
# second floow --> 1 4 10 20 ...

T = int(input())

ground_floor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


def roommate(list_in):
    next_floor = []
    tot = 0
    for i in range(14):
        tot += list_in[i]
        next_floor.append(tot)
    return next_floor


for i in range(T):
    k = int(input())
    n = int(input())
    next_floor = roommate(ground_floor)
    if k == 1:
        print(next_floor[n-1])
    elif k != 1:
        for i in range(k-1):
            next_floor = roommate(next_floor)
        print(next_floor[n-1])
