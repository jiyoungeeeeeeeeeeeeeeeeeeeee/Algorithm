T = int(input())

for t in range(T):
    n = int(input())
    dp = [0]*(max(4,n+1))

    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n]) 

