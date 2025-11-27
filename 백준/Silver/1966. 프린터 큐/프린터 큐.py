import sys
from collections import deque

T = int(sys.stdin.readline())

for t in range(T):
    n,l = map(int,sys.stdin.readline().strip().split())
    i = list(map(int,sys.stdin.readline().strip().split()))

    q = deque((v, idx) for idx, v in enumerate(i))

    cnt = 0
    while q:
        front = q[0]

        if front[0] < max(q)[0]:
            q.rotate(-1)
        else:
            cnt += 1
            v,idx = q.popleft()
            
            if idx == l:
                print(cnt)
                break
 