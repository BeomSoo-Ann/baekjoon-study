# No.2580 sudoku

from sys import stdin


N_dict = {}
for i in range(9):
    N_dict[i+1] = list(map(int, stdin.readline().split()))


def check_row(n):
    L = N_dict[n]
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

    L_list = sum(list(L.values()), [])

    if 0 in L_list:
        if L_list.count(0) == 1:
            zero_index = L_list.index(0)
            row = zero_index//3 + n-1
            col = zero_index % 3

            for i in range(1, 10):
                if i not in L_list:
                    N_dict[row][col] = i
    return


def check_box_456(n):
    L = {}
    L[n-1] = N_dict[n-1][3:6]
    L[n] = N_dict[n][3:6]
    L[n+1] = N_dict[n+1][3:6]

    L_list = sum(list(L.values()), [])

    if 0 in L_list:
        if L_list.count(0) == 1:
            zero_index = L_list.index(0)
            row = zero_index//3 + n-1
            col = zero_index % 3 + 3

            for i in range(1, 10):
                if i not in L_list:
                    N_dict[row][col] = i
    return


def check_box_789(n):
    L = {}
    L[n-1] = N_dict[n-1][6:]
    L[n] = N_dict[n][6:]
    L[n+1] = N_dict[n+1][6:]

    L_list = sum(list(L.values()), [])

    if 0 in L_list:
        if L_list.count(0) == 1:
            zero_index = L_list.index(0)
            row = zero_index//3 + n-1
            col = zero_index % 3 + 6

            for i in range(1, 10):
                if i not in L_list:
                    N_dict[row][col] = i

    return


def check_sudoku():
    # checking row
    check_row(1)
    check_row(2)
    check_row(3)
    check_row(4)
    check_row(5)
    check_row(6)
    check_row(7)
    check_row(8)
    check_row(9)

    # checking column
    check_col(1)
    check_col(2)
    check_col(3)
    check_col(4)
    check_col(5)
    check_col(6)
    check_col(7)
    check_col(8)
    check_col(9)

    # checking 3x3 box
    check_box_123(2)
    check_box_123(5)
    check_box_123(8)

    check_box_456(2)
    check_box_456(5)
    check_box_456(8)

    check_box_789(2)
    check_box_789(5)
    check_box_789(8)


while True:
    check_sudoku()
    S = sum(list(N_dict.values()), [])
    if 0 not in S:
        # print sudoku answer
        print(' '.join(str(num) for num in N_dict[1]))
        print(' '.join(str(num) for num in N_dict[2]))
        print(' '.join(str(num) for num in N_dict[3]))
        print(' '.join(str(num) for num in N_dict[4]))
        print(' '.join(str(num) for num in N_dict[5]))
        print(' '.join(str(num) for num in N_dict[6]))
        print(' '.join(str(num) for num in N_dict[7]))
        print(' '.join(str(num) for num in N_dict[8]))
        print(' '.join(str(num) for num in N_dict[9]))
        break

###############################################################################

graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))


def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True


def checkCol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True


def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0


dfs(0)
