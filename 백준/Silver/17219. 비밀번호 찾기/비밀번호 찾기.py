import sys

n,m = map(int,sys.stdin.readline().split())
lst = {}

for i in range(n):
    url,pw = sys.stdin.readline().split()
    lst[url] = pw 

for j in range(m):
    add = sys.stdin.readline().strip()
    print(lst.get(add))