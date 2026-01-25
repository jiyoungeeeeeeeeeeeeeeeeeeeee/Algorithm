import sys
from collections import Counter

n,c = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

ac = Counter(arr)
save = []
for k,v in ac.items():
    save.append((k,v))

save.sort(key = lambda x : (-x[1]))
result = []

for i,j in save:
    for _ in range(j):
        result.append(i)

print(*result)