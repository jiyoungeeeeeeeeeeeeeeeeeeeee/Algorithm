import sys

T = int(input())
nums = [int(sys.stdin.readline()) for _ in range(T)]
MAX = max(nums) + 1

dp = [0] * (MAX)
dp[0], dp[1], dp[2] = 1, 1, 2

for i in range(3, MAX):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for n in nums:
    print(dp[n])
