n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]
prefix = [[0] * 10 for _ in range(n + 1) ]

for j in range(10):
    dp[1][j] = 1
    prefix[1][j] = dp[1][j] if j == 0 else prefix[1][j-1] + dp[1][j]


for i in range(2, n + 1):
    for j in range(10):
        dp[i][j] = prefix[i-1][j] % 10007
        prefix[i][j] = dp[i][j] if j == 0 else (prefix[i][j-1] + dp[i][j]) % 10007

print(prefix[n][9])
