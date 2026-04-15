import sys

n, m = map(int, sys.stdin.readline().split())

basket = [0] * n

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())

    for a in range(i - 1, j):
        basket[a] = k

print(*basket)