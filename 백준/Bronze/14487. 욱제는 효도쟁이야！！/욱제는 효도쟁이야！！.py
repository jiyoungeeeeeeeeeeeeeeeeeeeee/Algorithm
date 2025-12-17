import sys
n = int(sys.stdin.readline())
vi = list(map(int,sys.stdin.readline().split()))

print(sum(vi) - max(vi))