import sys

n = int(sys.stdin.readline())
size = list(map(int,sys.stdin.readline().split()))
t,p = map(int,sys.stdin.readline().split())

tsum = 0

for s in size:
    tsum += (s+t-1) // t

ppack = n//p
pen = n%p

print(tsum)
print(ppack,pen)