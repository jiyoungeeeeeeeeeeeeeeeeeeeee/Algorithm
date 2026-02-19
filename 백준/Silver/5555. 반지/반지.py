import sys

find = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
cnt = 0

for i in range(n):
    ring = sys.stdin.readline().strip()
    h = 0

    while h < len(ring):
        if find in ring:
            cnt += 1
            break
        else:
            ring = ring[1:] + ring[:1]
            h += 1

print(cnt)