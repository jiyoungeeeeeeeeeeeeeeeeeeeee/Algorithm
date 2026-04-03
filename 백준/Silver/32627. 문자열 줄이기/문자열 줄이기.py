import sys

n, m = map(int, sys.stdin.readline().split())
s = list(sys.stdin.readline().strip())
order = []

for i in range(len(s)):
    order.append((s[i], i))

order.sort(key = lambda x: x[0])
order = order[m:]
order.sort(key = lambda x : x[1])

for k,v in order:
    print(k, end= '')