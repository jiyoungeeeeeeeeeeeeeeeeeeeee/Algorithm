import sys

n = int(sys.stdin.readline())

root = {}

for i in range(n):
    info = list(sys.stdin.readline().split())
    k,foods = int(info[0]), info[1:]

    cur = root
    for x in foods:
        if x not in cur:
            cur[x] = {}

        cur = cur[x]

def dfs(node, depth):
    for key in sorted(node.keys()):
        print('--' * depth + key)
        dfs(node[key], depth + 1)

dfs(root, 0)