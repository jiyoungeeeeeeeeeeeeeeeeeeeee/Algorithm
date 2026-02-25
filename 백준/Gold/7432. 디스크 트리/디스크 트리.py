import sys

n = int(sys.stdin.readline())
tree = dict()

for _ in range(n):
    direc = sys.stdin.readline().strip().split('\\')
    cur = tree

    for d in direc:
        if d not in cur:
            cur[d] = {}
        cur = cur[d]


def print_tree(node, depth):
    keys = sorted(node.keys())
    for k in keys:
        sys.stdout.write(" " * depth + k + "\n")
        print_tree(node[k], depth + 1)

print_tree(tree, 0)