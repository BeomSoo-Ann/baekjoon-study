# No.2580 sudoku

from sys import stdin


def check_zero(L):
    if 0 in L:
        if L.count(0) == 1:
            zero_index = L.index(0)
            for i in range(1, 10):
                if i not in L:
                    L[zero_index] = i
    else:
        pass
    return


def check_box():
    return


def check_sudoku():
    N_dict = {}

    for i in range(9):
        N_dict[i+1] = list(map(int, stdin.readline().split()))

    check_zero(N_dict[1])
    check_zero(N_dict[2])
    check_zero(N_dict[3])
    check_zero(N_dict[4])
    check_zero(N_dict[5])
    check_zero(N_dict[6])
    check_zero(N_dict[7])
    check_zero(N_dict[8])
    check_zero(N_dict[9])

    col_1 = [N_dict[i][0] for i in range(1, 10)]
    col_2 = [N_dict[i][1] for i in range(1, 10)]
    col_3 = [N_dict[i][2] for i in range(1, 10)]
    col_4 = [N_dict[i][3] for i in range(1, 10)]
    col_5 = [N_dict[i][4] for i in range(1, 10)]
    col_6 = [N_dict[i][5] for i in range(1, 10)]
    col_7 = [N_dict[i][6] for i in range(1, 10)]
    col_8 = [N_dict[i][7] for i in range(1, 10)]
    col_9 = [N_dict[i][8] for i in range(1, 10)]

    check_zero(col_1)
    check_zero(col_2)
    check_zero(col_3)
    check_zero(col_4)
    check_zero(col_5)
    check_zero(col_6)
    check_zero(col_7)
    check_zero(col_8)
    check_zero(col_9)

    for i in range(1, 10):
        print(N_dict[i])
    print(col_3)


check_sudoku()
