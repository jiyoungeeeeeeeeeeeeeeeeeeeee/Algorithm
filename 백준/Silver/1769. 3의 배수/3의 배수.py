import sys

x = sys.stdin.readline().strip()
cnt = 0
y = ['3','6','9']

while len(x) > 1:
    X = 0
    for u in x:
        u = int(u)
        X += u
    
    x = str(X)
    cnt += 1

print(cnt)

if x in y:
    print('YES')
else:
    print('NO')