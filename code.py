# No.11053 longest increasing sequence


from sys import stdin


N = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if base[i] > base[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
