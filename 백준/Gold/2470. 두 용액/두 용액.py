import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()

r = n-1
l = 0
m = abs(lst[0] + lst[-1])
best_l = l
best_r = r

while r > l:
    z = lst[r] + lst[l]

    if abs(z) < m :
        m = abs(z)
        best_l = l
        best_r = r

    if z < 0:
        l += 1
    elif z > 0:
        r -= 1
    elif z == 0:
        break

print(lst[best_l] , lst[best_r])