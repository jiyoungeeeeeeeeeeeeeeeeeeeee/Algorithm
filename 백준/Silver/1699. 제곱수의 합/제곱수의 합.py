n = int(input())
dp = [0]*(n+1)

dp[0] = 0

for i in range(1, n+1):
    dp[i] = i

    for j in range(1 , int(i**0.5) + 1):
        dp[i] = min(dp[i] , dp[i-j*j] + 1)

print(dp[n])
