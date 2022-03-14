# No.1463 OUTPUT 1


from sys import stdin


N = int(stdin.readline())
dp = [0] * (10**6 + 1)


dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 3
dp[6] = 2
dp[7] = 3
dp[8] = 3
dp[9] = 2
dp[10] = 3


if N <= 10:
    print(dp[N])

elif N > 10:
    for i in range(11, N+1):
        dp[i] = dp[i-1]+1

        if i % 3 == 0:
            dp[i] = min(dp[i//3]+1, dp[i])
        if i % 2 == 0:
            dp[i] = min(dp[i//2]+1, dp[i])

    print(dp[N])
############################################
n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])
