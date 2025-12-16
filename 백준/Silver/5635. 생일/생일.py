import sys

n = int(sys.stdin.readline())

info = []
for i in range(n):
    name,d,m,y = sys.stdin.readline().split()
    d = int(d)
    m = int(m)
    y = int(y)

    info.append((name,d,m,y))

info.sort(key = lambda x:(x[3], x[2] , x[1]))
print(info[-1][0])
print(info[0][0])
    