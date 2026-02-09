import sys
from collections import deque

n = int(sys.stdin.readline())
cnt = 0
seen = set()

for _ in range(n):
    word = sys.stdin.readline().strip()
    dq = deque(word)

    best = word
    k = 1

    while k < len(word):
        dq.rotate(-1)
        rotated = ''.join(dq)

        if rotated < best:
            best = rotated
        
        k += 1
    
    seen.add(best)

print(len(seen))
    