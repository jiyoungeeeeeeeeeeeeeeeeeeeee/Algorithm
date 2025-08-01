n = int(input())
p = [0] + list(map(int, input().split()))  # 1-based 인덱싱

dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + p[j])

print(dp[n])
