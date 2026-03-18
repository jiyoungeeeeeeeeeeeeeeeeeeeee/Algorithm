import sys

a,b = map(int,sys.stdin.readline().split())

cnt = 0

while b > a:

    if b % 2 == 0:
        b = b//2
        cnt += 1 

    elif b % 2 != 0 and str(b)[-1] == '1':
        b = int(str(b)[:-1])
        cnt += 1
    else:
        break

if b == a:
    print(cnt+1)
else:
    print(-1)