n = int(input())

dp = [[0] * 10 for _ in range(n+1)]

dp[1][0] = 0
result = []

for j in range(1, 10):
    dp[1][j] = 1


for i in range(1,n+1):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i-1][j-1]
        if j < 9:
            dp[i][j] += dp[i-1][j+1]

result = sum(dp[n][j] for j in range(10))
print(result % 1000000000)