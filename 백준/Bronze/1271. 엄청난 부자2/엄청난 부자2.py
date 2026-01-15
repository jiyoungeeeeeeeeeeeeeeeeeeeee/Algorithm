import sys

n,m = map(int,sys.stdin.readline().split())

a = n//m
b = n%m

print(a,b , sep= '\n')