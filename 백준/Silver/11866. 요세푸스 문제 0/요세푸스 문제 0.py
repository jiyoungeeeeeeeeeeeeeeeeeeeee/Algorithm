from collections import deque
import sys

dq = deque()
n,k = map(int,sys.stdin.readline().split())

for i in range(1,n+1):
    dq.append(i)

result = []

for _ in range(n):
    dq.rotate(-k)
    result.append(dq.pop())

print("<" + ', '.join(map(str,result)) + '>')
