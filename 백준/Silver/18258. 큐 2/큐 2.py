import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()

for i in range(n):
    command = sys.stdin.readline().split()
    com = command[0]
    
    if com == "push":
        dq.append(command[1])
    elif com == 'pop':
        if dq:
            print(dq[0])
            dq.popleft()
        else:
            print(-1)
    elif com == 'size':
        print(len(dq))
    elif com == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif com == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif com == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)