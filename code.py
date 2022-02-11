# No.2580 sudoku

from sys import stdin


N_dict = {}
for i in range(9):
    N_dict[i+1] = list(map(int, stdin.readline().split()))


def check_row(L):
    if 0 in L:
        if L.count(0) == 1:
            zero_index = L.index(0)
            for i in range(1, 10):
                if i not in L:
                    L[zero_index] = i
    else:
        pass
    return


def check_col(n):
    L = []
    for i in range(1, 10):
        L.append(N_dict[i][n-1])

    if 0 in L:
        if L.count(0) == 1:
            zero_index = L.index(0)
            for i in range(1, 10):
                if i not in L:
                    N_dict[zero_index+1][n-1] = i
    else:
        pass
    return


def check_box_123(n):
    L = {}
    L[n-1] = N_dict[n-1][:3]
    L[n] = N_dict[n][:3]
    L[n+1] = N_dict[n+1][:3]
    print(L)
    return


def check_box_456(n):
    L = {}
    L[n-1] = N_dict[n-1][3:6]
    L[n] = N_dict[n][3:6]
    L[n+1] = N_dict[n+1][3:6]
    print(L)
    return


def check_box_789(n):
    L = {}
    L[n-1] = N_dict[n-1][6:]
    L[n] = N_dict[n][6:]
    L[n+1] = N_dict[n+1][6:]
    print(L)
    return


def check_sudoku():
    print(N_dict)

    check_row(N_dict[1])
    check_row(N_dict[2])
    check_row(N_dict[3])
    check_row(N_dict[4])
    check_row(N_dict[5])
    check_row(N_dict[6])
    check_row(N_dict[7])
    check_row(N_dict[8])
    check_row(N_dict[9])

    check_col(1)
    check_col(2)
    check_col(3)
    check_col(4)
    check_col(5)
    check_col(6)
    check_col(7)
    check_col(8)
    check_col(9)

    check_box_123(2)
    check_box_456(2)
    check_box_789(2)
    check_box_123(5)
    check_box_456(5)
    check_box_789(5)
    check_box_123(8)
    check_box_456(8)
    check_box_789(8)


check_sudoku()
