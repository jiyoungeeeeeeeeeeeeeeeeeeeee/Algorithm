import sys
from collections import deque

dq = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().strip()

    if command.startswith('push_front'):
        _, num = command.split()
        dq.appendleft(num)

    elif command.startswith('push_back'):
        _, num = command.split()
        dq.append(num)

    elif command == 'pop_front':
        print(dq.popleft() if dq else -1)

    elif command == 'pop_back':
        print(dq.pop() if dq else -1)

    elif command == 'size':
        print(len(dq))

    elif command == 'empty':
        print(0 if dq else 1)

    elif command == 'front':
        print(dq[0] if dq else -1)

    elif command == 'back':
        print(dq[-1] if dq else -1)
