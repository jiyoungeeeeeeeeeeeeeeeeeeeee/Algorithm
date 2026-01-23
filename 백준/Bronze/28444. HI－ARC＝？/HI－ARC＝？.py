import sys

h,i,a,r,c = map(int,sys.stdin.readline().split())

f = h * i
s = a * r * c

print(f-s)