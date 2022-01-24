# 1018 Chess coloring

from sys import stdin

M, N = map(int, stdin.readline().split())

BASE_B = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], [
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
BASE_W = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], [
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

SQUARE = [list(map(str, stdin.readline().strip())) for _ in range(M)]


def COUNT_ERROR(BOARD, BASE):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if BOARD[i][j] != BASE[i][j]:
                cnt += 1
            else:
                pass
    return cnt


def MAKE_8X8(BOARD, col_start, row_start):
    NEW_BOARD = []
    for i in range(row_start, row_start + 8):
        NEW_BOARD.append(BOARD[i][col_start:col_start + 8])
    return NEW_BOARD


ERROR_LIST = []

for i in range(M-7):
    for j in range(N-7):
        BOARD = MAKE_8X8(SQUARE, j, i)
        ERROR_LIST.append(COUNT_ERROR(BOARD, BASE_B))
        ERROR_LIST.append(COUNT_ERROR(BOARD, BASE_W))


print(min(ERROR_LIST))