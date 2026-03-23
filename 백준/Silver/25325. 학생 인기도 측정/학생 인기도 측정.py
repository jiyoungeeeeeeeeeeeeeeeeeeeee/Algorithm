import sys
from collections import Counter

n = int(sys.stdin.readline())
names = list(sys.stdin.readline().split())
c = Counter()
result = []

for _ in range(n):
    love = sys.stdin.readline().split()
    c.update(love)

blank = set(c)
orgin = set(names)
missing = orgin-blank

for m in missing:
    result.append((m , 0))

for k,v in sorted(c.items()):
    result.append((k,v))

result.sort(key = lambda x : (-x[1] , x[0]))

for r in result:
    print(*r)
    