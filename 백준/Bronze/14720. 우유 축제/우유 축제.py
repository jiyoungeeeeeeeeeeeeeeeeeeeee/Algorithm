import sys
from collections import deque

n = int(sys.stdin.readline())
store = list(map(int,sys.stdin.readline().split()))
cnt =  0
milk = deque([0,1,2])

for i in store:
    if i == milk[0]:
        cnt += 1
        milk.rotate(-1)

print(cnt) 