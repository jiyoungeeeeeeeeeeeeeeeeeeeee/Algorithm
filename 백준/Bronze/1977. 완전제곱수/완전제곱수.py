import sys,math

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
result = []

for i in range(m,n+1):
    root = math.isqrt(i)
    if root * root == i:
        result.append(i)

if result :
    print(sum(result),min(result), sep = '\n')
else:
    print(-1)