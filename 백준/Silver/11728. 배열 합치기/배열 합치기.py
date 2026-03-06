import sys

n,m = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

result= a+b
r = sorted(result)
print(*r)