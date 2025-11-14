import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

res   = 0
pairs = [(value,index) for index,value in enumerate(b)]

a.sort()
pairs.sort(reverse = True)

for i in range(n):
    res += a[i] * b[pairs[i][1]]

print(res)