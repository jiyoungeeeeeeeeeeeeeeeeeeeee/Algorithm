n = int(input())

A = list(map(int,input().split()))
dp = [1]*(n+1)

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
    