# No.2156 Wine tasting


from sys import stdin


N = int(stdin.readline())
wines = [int(stdin.readline()) for _ in range(N)]
dp = [0] * 10001

if N == 1:
    print(wines[0])
elif N == 2:
    print(wines[0] + wines[1])
else:
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(wines[0] + wines[2], wines[1] + wines[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2]+wines[i], max(dp[:i-2]) +
                    wines[i-1]+wines[i], max(dp))

    print(max(dp))
