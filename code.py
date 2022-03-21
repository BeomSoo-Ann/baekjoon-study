# No.11054 longest "bytonic" increasing sequence


from sys import stdin


N = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
reverse_base = base[::-1]

dp = [1] * N
reverse_dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if base[i] > base[j]:
            dp[i] = max(dp[i], dp[j]+1)

for i in range(1, N):
    for j in range(i):
        if reverse_base[i] > reverse_base[j]:
            reverse_dp[i] = max(reverse_dp[i], reverse_dp[j]+1)

result = [0] * N

for i in range(N):
    result[i] = dp[i] + reverse_dp[N-i-1] - 1


print(max(result))
