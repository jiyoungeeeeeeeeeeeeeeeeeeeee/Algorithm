import sys

n = int(sys.stdin.readline())
lst = [i for i in range(n,0,-1)]
m = list(map(int,sys.stdin.readline().split()))
result = []
idx = 0

for w in m[::-1]:
    result.insert(w,lst[idx])
    idx += 1

print(*result)
