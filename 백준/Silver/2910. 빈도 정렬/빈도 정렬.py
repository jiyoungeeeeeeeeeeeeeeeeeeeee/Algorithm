import sys

n,c = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

ac = {}

for i in arr:
    if i not in ac:
        ac[i] = 1
    else:
        ac[i] += 1

result = sorted(ac.items(), key = lambda x : (-x[1]))

for i,j in result:
    for _ in range(j):
        print(i, end = ' ')