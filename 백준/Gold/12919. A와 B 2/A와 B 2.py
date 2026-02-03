import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
ans = 0

def dfs(cur):
    global ans
    if ans == 1:
        return
    if len(cur) == len(s):
        if cur == s:
            ans = 1
        return

    if cur[-1] == 'A':
        dfs(cur[:-1])

    if cur[0] == 'B':
        dfs(cur[1:][::-1])

dfs(t)
print(ans)
