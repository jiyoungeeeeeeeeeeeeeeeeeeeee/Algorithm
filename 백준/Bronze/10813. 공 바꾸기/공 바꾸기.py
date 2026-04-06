import sys

n,m = map(int,sys.stdin.readline().split())
bags = []
for i in range(1,n+1):
    bags.append(i)

for change in range(m):
    i, j = map(int, input().split())
    bags[i-1], bags[j-1] = bags[j-1], bags[i-1]

for bag in bags:
    print(bag, end=' ')