import sys
cnt = 0
while True:
    n = int(sys.stdin.readline())
    
    if n == 0:
        break

    nord = {}
    for i in range(1,n+1):
        name = sys.stdin.readline().strip()
        nord[i] = name 
   
    lst = []
    for _ in range(2*n-1):
        a,b = sys.stdin.readline().split()
        a = int(a)

        if a not in lst:
            lst.append(a)
        else:
            lst.remove(a)
    
    for l in lst:
        cnt += 1
        print( cnt ,nord[l])