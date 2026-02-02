import sys

n, m = map(int, sys.stdin.readline().split())
chosen = []

def dfs(start):
    if len(chosen) == m:
        sys.stdout.write(" ".join(map(str, chosen)) + "\n")
        return

    x = start
    while x <= n:
        chosen.append(x)
        dfs(x + 1)
        chosen.pop()
        x += 1

dfs(1)
