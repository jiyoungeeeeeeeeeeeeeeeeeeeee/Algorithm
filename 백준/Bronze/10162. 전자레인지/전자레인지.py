import sys

t = int(sys.stdin.readline())
cnt5 = 0
cnt1 = 0
cnt0 = 0

if t % 10 != 0:
    print(-1)

else:
    while t > 0:
        if t >= 300:
            t -= 300
            cnt5 += 1
        elif t >= 60 and t < 300:
            t -= 60
            cnt1 += 1
        elif t >= 10 and t < 60:
            t -= 10
            cnt0 += 1

    print(cnt5, cnt1, cnt0)

    
    
    