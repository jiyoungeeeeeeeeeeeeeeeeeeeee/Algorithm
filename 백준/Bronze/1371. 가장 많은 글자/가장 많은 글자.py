import sys
from collections import Counter

c = Counter()

while True:
    text = sys.stdin.readline()
    if not text:
        break
    for t in text:
        if 'a' <= t <= 'z':    
            c[t] += 1
result = []
max_value = max(c.values())

for k,v in c.items():
    if v == max_value:
        result.append(k)
result.sort()
print(''.join(result))
