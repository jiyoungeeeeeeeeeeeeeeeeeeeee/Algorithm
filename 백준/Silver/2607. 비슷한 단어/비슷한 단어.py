import sys
from collections import Counter

n = int(sys.stdin.readline())
f = Counter(sys.stdin.readline().strip())
cnt = 0

for _ in range(n-1):
    s = Counter(sys.stdin.readline().strip())
    a = s-f
    b = f-s
    
    if sum(a.values()) <= 1 and sum(b.values()) <= 1:
        cnt += 1

print(cnt)    