import sys

a,b,c,n = map(int,sys.stdin.readline().split())
dp = [False] * (n+1)
dp[0] = True

for i in range(n+1):
    if dp[i] == True:
        if i+a <= n: dp[i+a] = True
        if i+b <= n: dp[i+b] = True
        if i+c <= n: dp[i+c] = True

if dp[-1] == True:
    print(1)
else:
    print(0)