import sys

n = sys.stdin.readline().strip()
r = n[(len(n)//2):]
l = n[:(len(n)//2)]

tr = 0
tl = 0

for i in range(len(r)):
    tr += int(r[i])
    tl += int(l[i])

if tr == tl:
    print('LUCKY')

else:
    print('READY')