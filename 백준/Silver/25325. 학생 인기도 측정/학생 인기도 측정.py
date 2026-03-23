import sys
from collections import Counter

n = int(sys.stdin.readline())
names = sys.stdin.readline().split()
c = Counter()

for _ in range(n):
    love = sys.stdin.readline().split()
    c.update(love)

result = []

for name in names:
    result.append((name, c[name]))

result.sort(key=lambda x: (-x[1], x[0]))

for name, count in result:
    print(name, count)