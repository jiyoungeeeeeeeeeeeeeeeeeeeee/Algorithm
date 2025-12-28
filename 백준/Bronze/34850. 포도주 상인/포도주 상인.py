import sys

x,y,p,a,b = list(map(int,sys.stdin.readline().split()))

price = (y-1)*b + p
income = 0

for i in range(x):
    income += price-(a*i)

print(income)