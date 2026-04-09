import sys

n,k = map(int,sys.stdin.readline().split())
weight = list(map(int,sys.stdin.readline().split()))
weight.sort()

r = n-1
l = 0
cnt = 0

while l < r :
    t = weight[r] + weight[l]
    if t <= k :
        cnt +=1
        l +=1
    r -= 1

print(cnt)
