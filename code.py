# No.2579 stairs

from sys import stdin


N = int(stdin.readline())
stair = [0] * 300
for i in range(N):
    stair[i] = int(stdin.readline())

dp = [0] * 300

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = stair[2] + max(dp[1], dp[0])

if N == 1:
    print(dp[0])
elif N == 2:
    print(dp[1])
elif N == 3:
    print(dp[2])
else:
    for i in range(3, N):
        dp[i] = max(stair[i]+dp[i-2], stair[i]+dp[i-3]+stair[i-1])

    print(dp)
    print(dp[N-1])
    