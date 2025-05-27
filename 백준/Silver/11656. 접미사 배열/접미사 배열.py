import sys
from collections import deque

S = sys.stdin.readline().rstrip()
s_dq = deque(S)
stack = [s_dq.copy()] # 처음 상태 포함

for s in range (len(S)-1):
    s_dq.popleft()
    stack.append(s_dq.copy())

result = [''.join(d) for d in stack]
sorted_result = sorted(result)

for r in sorted_result:
    print(r)

