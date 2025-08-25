import sys
input = sys.stdin.readline
n,m = map(int,input().split())

listen = set()
see = set()

for _ in range(n):
    l = input().strip()
    listen.add(l)

for _ in range(m):
    s = input().strip()
    see.add(s)

same = sorted(listen & see)
print(len(same))
print(*same , sep= '\n')
