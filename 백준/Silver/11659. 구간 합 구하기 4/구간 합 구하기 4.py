import sys

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

accumulate = [0] * (n+1)
i = 1

while i <= n:
    accumulate[i] = arr[i-1] + accumulate[i-1]
    i += 1

for _ in range(m):
    t,y = map(int,sys.stdin.readline().split())
    print(accumulate[y] - accumulate[t-1])    