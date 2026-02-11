import sys
from collections import Counter
n = int(sys.stdin.readline())

pl = []
for _ in range(n):
    participant = sys.stdin.readline().strip()
    pl.append(participant)

cnt1 = Counter(pl)

cl = []
for _ in range(n-1):
    complete = sys.stdin.readline().strip()
    cl.append(complete)
cnt2 = Counter(cl)

print(*cnt1 - cnt2)
