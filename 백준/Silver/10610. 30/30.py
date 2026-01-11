import sys

n = sys.stdin.readline().strip()
a = 0

for i in n:
    a += int(i)

if '0' in n and a%3 == 0:
    n = list(n)
    n.sort(reverse = True)
    print(*n , sep='')    

else:
    print(-1)    