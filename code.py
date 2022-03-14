# No.1149 RGB street

from sys import stdin


N = int(stdin.readline())
tri = [list(map(int, stdin.readline().split())) for _ in range(N)]

if N == 1:
    print(tri[0][0])
    exit()


tri[1][0] += tri[0][0]
tri[1][1] += tri[0][0]


for i in range(2, N):
    for j in range(i+1):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])


print(max(tri[-1]))
