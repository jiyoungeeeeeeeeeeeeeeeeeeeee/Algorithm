import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

total = 0

for i in range(n):
    if a[i] - b[i] < 0:
        total += abs(a[i] - b[i])
print(total)