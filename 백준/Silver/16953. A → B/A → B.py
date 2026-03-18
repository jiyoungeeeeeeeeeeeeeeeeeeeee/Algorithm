import sys

a,b = map(int,sys.stdin.readline().split())

cnt = 0

while b > a:

    if b % 2 == 0:
        b = b//2
        cnt += 1 

    elif b % 10 == 1:
        b //= 10
        cnt += 1
    else:
        break

if b == a:
    print(cnt+1)
else:
    print(-1)