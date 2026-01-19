import sys,math

a,b = map(int,sys.stdin.readline().split(':'))
g = math.gcd(a,b)

print(a//g,':',b//g ,sep = '')