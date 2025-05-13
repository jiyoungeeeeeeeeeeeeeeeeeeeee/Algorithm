import sys

n = int(sys.stdin.readline().strip())
q = []

for i in range(n):
    commend = sys.stdin.readline().strip()

    if 'push' in commend:
        _,num = commend.split()
        q.append(num)

    if 'pop' in commend:
        if q :
            print(q[0])
            q.pop(0)
        else:
            print(-1)
    if 'size' in commend:
        print(len(q))

    if 'empty' in commend:
        if q :
            print(0)
        else:
            print(1)
    if 'front' in commend:
        if q :
            print(q[0])            
        else:
            print(-1)
    if 'back' in commend:
        if q  :
            print(q[-1])
        else:
            print(-1)

    

