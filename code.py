# No.1149 RGB street

from sys import stdin


N = int(stdin.readline())
cache = [list(map(int, stdin.readline().split())) for _ in range(N)]


for i in range(1, N):
    cache[i][0] += min(cache[i-1][1], cache[i-1][2])
    cache[i][1] += min(cache[i-1][0], cache[i-1][2])
    cache[i][2] += min(cache[i-1][0], cache[i-1][1])

print(min(cache[-1]))
