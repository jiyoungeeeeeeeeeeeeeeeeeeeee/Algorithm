import sys

n,m = map(int,sys.stdin.readline().split())
lst = [i for i in range(1,n+1)]

result = []
idx = 0

def dfs(start):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(start, n+1):
        result.append(i)
        dfs(i)
        result.pop()

dfs(1)
        