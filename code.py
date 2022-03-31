# No.9251 Longest Common Subsequence


from sys import stdin


str_list = [stdin.readline().strip() for _ in range(2)]
dp = [0] * len(str_list[0])

for i in range(len(str_list[1])):
    cnt = 0
    for j in range(len(str_list[0])):
        if dp[j] > cnt:
            cnt = dp[j]

        if str_list[1][i] == str_list[0][j]:
            dp[j] = cnt + 1

print(dp)
