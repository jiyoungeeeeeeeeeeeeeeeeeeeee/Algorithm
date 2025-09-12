import sys
n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

keep = [0] * n
drop = [0] * n

keep[0] = num[0]
drop[0] = -10**9

for i in range(1,n):
    keep[i] = max(num[i] , keep[i-1] + num[i])
    drop[i] = max(drop[i-1] + num[i] , keep[i-1])

print(max(max(keep), max(drop)))
