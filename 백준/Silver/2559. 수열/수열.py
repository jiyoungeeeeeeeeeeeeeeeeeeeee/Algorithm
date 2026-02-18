import sys

n,k = map(int,sys.stdin.readline().split())
temp = list(map(int,sys.stdin.readline().split()))
window = sum(temp[:k])
best = window

for i in range(k,n):
    window += temp[i]
    window -= temp[i-k]
    best = max(best, window)

print(best)