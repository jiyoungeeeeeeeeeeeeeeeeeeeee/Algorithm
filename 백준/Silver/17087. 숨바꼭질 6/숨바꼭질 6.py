import sys
from math import gcd
from functools import reduce
N,S = map(int,sys.stdin.readline().strip().split())
location = list(map(int,sys.stdin.readline().split()))

sisters = []

for loc in location:
    sisters.append(abs(loc-S))

result = reduce(gcd, sisters)
print(result)