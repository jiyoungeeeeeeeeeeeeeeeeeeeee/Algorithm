import sys

t = int(sys.stdin.readline())

for _ in range(t):
    N,W = sys.stdin.readline().split()
    n = int(N)
    
    w = list(W)
    w.pop(n-1)
    print(*w,sep = '')