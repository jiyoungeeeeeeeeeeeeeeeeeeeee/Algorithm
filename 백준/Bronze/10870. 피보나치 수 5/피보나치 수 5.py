n = int(input())
MAX = 20
dp = [0]*(MAX+1)

dp[0] = 0
dp[1] = 1

for i in range(2,MAX+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])