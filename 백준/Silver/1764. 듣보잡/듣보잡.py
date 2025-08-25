import sys
input = sys.stdin.readline
n,m = map(int,input().split())

listen = {input().strip() for _ in range(n)}
see = {input().strip() for _ in range(m)}

same = sorted(listen & see)
print(len(same))
print(*same , sep = '\n')