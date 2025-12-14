import sys

n,m = map(int,sys.stdin.readline().split())

for i in range(n):
    fish = sys.stdin.readline().strip()
    print(fish[::-1])
    