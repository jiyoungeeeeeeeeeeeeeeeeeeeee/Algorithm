import sys
from collections import Counter

n = int(sys.stdin.readline())
names = list(sys.stdin.readline().split())
c = Counter()
result = []

for _ in range(n):
    love = sys.stdin.readline().split()
    c.update(love)

cname = set(c)
origin = set(names)
missing = origin-cname

for m in missing:
    result.append((m , 0))

for k,v in c.items():
    result.append((k,v))

result.sort(key = lambda x : (-x[1] , x[0]))

for r in result:
    print(*r)
    