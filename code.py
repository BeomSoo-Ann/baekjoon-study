# No.9251 Longest Common Subsequence


from sys import stdin


str_list = [stdin.readline().strip() for _ in range(2)]
L = []

for i in str_list[0]:
    for j in range(len(str_list[1])):
        if i == str_list[1][j]:
            L.append(j)

dp = [1] * len(L)

for i in range(1, len(L)):
    for j in range(i):
        if L[i] > L[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
