a = int(input())
arr = list(map(int,input().split()))

dp = [1]*a
prev = [-1]*a

for i in range(a):
    for j in range(i):
        if arr[j] < arr[i] and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1
            prev[i] = j  

length = max(dp)
print(length)

idx = dp.index(length)
lis = []
while idx != -1:
    lis.append(arr[idx])
    idx = prev[idx]
lis.reverse()
print(*lis)
