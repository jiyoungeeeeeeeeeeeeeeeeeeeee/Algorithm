from collections import deque
import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().strip().split()))
stack = []
result = [-1] * n

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)



sys.stdout.write(' '.join(map(str, result)))

        