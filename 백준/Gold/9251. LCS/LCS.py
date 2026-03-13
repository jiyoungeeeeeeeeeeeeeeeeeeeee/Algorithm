import sys

text1 = sys.stdin.readline().strip()
text2 = sys.stdin.readline().strip()

dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
dp[0][0] = 0

for i in range(len(text2)):
    for j in range(len(text1)):
        
        if text2[i] == text1[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[-1][-1])