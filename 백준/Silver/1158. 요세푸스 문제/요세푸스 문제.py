import sys

n,k = map(int,sys.stdin.readline().strip().split())
yo = []
order_list = []
index = 0

for i in range(1,n+1):
    yo.append(i)

while yo:
    index = (index + k-1) % len(yo)
    order_list.append(yo.pop(index))

print('<'+', '.join(map(str,order_list)) + '>')
