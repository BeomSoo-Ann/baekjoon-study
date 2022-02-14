# No.14888 plus minus multiply divide

from sys import stdin


N = int(stdin.readline())
num_list = list(map(int, stdin.readline().split()))
arithmetic_count = list(map(int, stdin.readline().split()))
L = []
tot_list = []


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a < 0 or b < 0:
        return (abs(a)//abs(b))*(-1)
    else:
        return a // b


def backtracking():
    if len(L) == N-1:
        calc_list = []
        calc_list.append(num_list[0])
        for i in range(N-1):
            if L[i] == 0:
                calc_list.append(add(calc_list[-1], num_list[i+1]))
            elif L[i] == 1:
                calc_list.append(sub(calc_list[-1], num_list[i+1]))
            elif L[i] == 2:
                calc_list.append(mul(calc_list[-1], num_list[i+1]))
            elif L[i] == 3:
                calc_list.append(div(calc_list[-1], num_list[i+1]))
        tot_list.append(calc_list[N-1])
        return

    for i in range(4):
        if arithmetic_count[i] > 0:
            if L.count(i) < arithmetic_count[i]:
                L.append(i)
                backtracking()
                L.pop()


backtracking()
print(max(tot_list))
print(min(tot_list))
