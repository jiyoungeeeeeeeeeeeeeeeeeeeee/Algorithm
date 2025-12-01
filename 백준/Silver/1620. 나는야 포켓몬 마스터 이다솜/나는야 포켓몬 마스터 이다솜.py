import sys
n,m = map(int,sys.stdin.readline().split())

title = {}
idx = {}

for i in range(1,n+1):
    name = sys.stdin.readline().rstrip()
    title[name] = i
    idx[i] = name


for _ in range(m):
    test = sys.stdin.readline().strip()
    if test.isnumeric():
        print(idx[int(test)])
    else:
        print(title.get(test))

