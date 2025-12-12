import sys
from collections import deque

n = int(sys.stdin.readline())
balloon = map(int,sys.stdin.readline().split())
lst = []
result = []

for idx,bal in enumerate(balloon , start = 1):
    lst.append((idx,bal))
dq = deque(lst)

while dq:
    idx,move = dq.popleft()
    result.append(idx)

    if not dq:
        break
    
    if move > 0:
        dq.rotate(-(move-1))
    else:
        dq.rotate(-move)

print(*result)