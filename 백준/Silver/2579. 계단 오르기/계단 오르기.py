n = int(input())
stairs = [int(input()) for i in range(n)]

dp = [0]*n  
dp[0] = stairs[0]

if n >= 2:
    dp[1] = stairs[0] + stairs[1]

if n >= 3:
    dp[2] = max(stairs[0] + stairs[2] , stairs[1] + stairs[2])


for i in range(3,n):
    dp[i] = max(dp[i-2] , dp[i-3] + stairs[i-1]) + stairs[i]

print(dp[n-1])