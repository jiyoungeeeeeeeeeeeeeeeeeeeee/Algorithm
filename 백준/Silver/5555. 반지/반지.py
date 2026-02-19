import sys

find = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
cnt = 0

for i in range(n):
    ring = sys.stdin.readline().strip()
    if find in (ring + ring):
        cnt += 1
    
print(cnt)