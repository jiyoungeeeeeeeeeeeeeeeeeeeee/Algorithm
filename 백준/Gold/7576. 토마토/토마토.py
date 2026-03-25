import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())
box = deque()
graph = []

for i in range(n):
    tomato = list(map(int,sys.stdin.readline().split()))
    graph.append(tomato)

    for t in range(len(tomato)):
        if tomato[t] == 1:
            box.append((i,t))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while box:
    r,c = box.popleft()

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < m:
            if graph[nr][nc] == 0:
                graph[nr][nc] = graph[r][c] + 1
                box.append((nr,nc))
MAX = []

for g in graph:
    if 0 in g:
        print(-1)
        break
    else:
        MAX.append(max(g))
else:
    print(max(MAX)-1)