import sys

n = int(sys.stdin.readline().strip())
nge = list(map(int,sys.stdin.readline().split()))
stack = []
result = [-1] * n # 오큰수를 못 찾으면 기본값 -1 넣어둠

for i in range(n):
    while stack and nge[stack[-1]] < nge[i]: 
            result[stack.pop()] = nge[i]
    stack.append(i)

print(*result)
