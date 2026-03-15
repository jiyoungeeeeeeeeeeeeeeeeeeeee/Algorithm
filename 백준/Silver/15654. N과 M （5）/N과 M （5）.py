import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()
result = []
visited = [False] * n

def dt():
    if len(result) == m:
        print(*result)
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            result.append(lst[i])

            dt()

            result.pop()
            visited[i] = False

dt()