# No.11054 longest "bytonic" increasing sequence


from sys import stdin


N = int(stdin.readline())
wire = [list(map(int, stdin.readline().split())) for _ in range(N)]
wire.sort()

end_point = [wire[i][1] for i in range(N)]
dp = [1] * N


for i in range(1, N):
    for j in range(i):
        if end_point[i] > end_point[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
