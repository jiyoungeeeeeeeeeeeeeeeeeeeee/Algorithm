import sys

s = sys.stdin.readline().strip()
q = int(sys.stdin.readline())

for i in range(q):
    a,l,r = sys.stdin.readline().split()
    l,r = int(l),int(r)
    cnt = s[l:r+1].count(a)
    print(cnt)