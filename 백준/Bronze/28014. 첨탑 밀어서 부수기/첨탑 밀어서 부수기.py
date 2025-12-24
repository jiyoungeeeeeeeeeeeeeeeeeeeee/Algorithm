import sys

n = int(sys.stdin.readline())
h = list(map(int,sys.stdin.readline().split()))
cnt = 1

for i in range(n-1):
    if h[i] <= h[i+1]:
        cnt += 1

print(cnt)