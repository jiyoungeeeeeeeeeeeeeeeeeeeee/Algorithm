import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()

r = n-1
l = 0
m = abs(lst[0] + lst[-1])
idx = []

while r > l:
    z = lst[r] + lst[l]

    if abs(z) < m :
        m = abs(z)
        idx.append((l,r))

    if z < 0:
        l += 1
    elif z > 0:
        r -= 1
    elif z == 0:
        break
        
if idx:
    print(lst[idx[-1][0]] , lst[idx[-1][1]] )
else:
    print(lst[0] , lst[-1])