import sys

n = int(sys.stdin.readline())
dp = []
tri = []

for i in range(n):
    tri.append(list(map(int,sys.stdin.readline().split())))
    dp.append([0] * (i+1))


for i in range(n):
    for j in range(i+1):
        if i == 0 and j == 0:
            dp[i][j] = tri[i][j]
        elif j == 0:
            dp[i][j] = tri[i][j] + dp[i-1][j]
        elif i == j:
            dp[i][j] = tri[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = tri[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[n-1]))