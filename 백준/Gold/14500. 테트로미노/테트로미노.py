import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = []
for _ in range(n):
    visited.append([False] * m)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_val = 0
for i in range(n):
    for j in range(m):
        if board[i][j] > max_val:
            max_val = board[i][j]

best = 0

def dfs(x, y, depth, total):
    global best

    # 가지치기: 앞으로 남은 칸을 전부 max_val로 채워도 best 못 넘으면 중단
    if total + (4 - depth) * max_val <= best:
        return

    if depth == 4:
        if total > best:
            best = total
        return

    k = 0
    while k < 4:
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, depth + 1, total + board[nx][ny])
                visited[nx][ny] = False
        k += 1

def check_t(x, y):
    global best
    # 중심 (x,y) + 주변 4방향 중 3개 선택(= 4개 합에서 하나 빼기)
    center = board[x][y]
    cnt = 0
    s = center
    min_arm = 10**9

    k = 0
    while k < 4:
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            cnt += 1
            val = board[nx][ny]
            s += val
            if val < min_arm:
                min_arm = val
        k += 1

    # 팔이 3개 미만이면 T자 불가능
    if cnt < 3:
        return

    # 팔이 3개면 그대로가 T자
    if cnt == 3:
        if s > best:
            best = s
        return

    # 팔이 4개면 4개 중 하나를 빼서 3개 선택
    s -= min_arm
    if s > best:
        best = s

i = 0
while i < n:
    j = 0
    while j < m:
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

        check_t(i, j)
        j += 1
    i += 1

print(best)
