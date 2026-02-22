import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    result = []
    for _ in range(n):
        pn = sys.stdin.readline().strip()
        result.append(pn)
    result.sort()

    ok = True

    for i in range(n-1):
        if result[i+1].startswith(result[i]):
            ok = False
    
    if ok:
        print('YES')
    else:
        print('NO')