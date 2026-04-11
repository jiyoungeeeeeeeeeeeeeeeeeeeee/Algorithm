import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    m = list(sys.stdin.readline().strip())
    lst.append(m)

k = int(sys.stdin.readline())

if k == 1:
    for l in lst:
        print(*l,sep='')

elif k == 2:
    for l in lst:
        print(*l[::-1],sep='')
    
elif k == 3:
    for l in lst[::-1]:
        print(*l,sep='')

