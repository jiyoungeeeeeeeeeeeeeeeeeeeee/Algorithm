import sys
from collections import deque

n = int(sys.stdin.readline())

cards = deque([i for i in range(1,n+1)])

# left = []
# trash = []

while len(cards) >= 1:
    t = cards.popleft()
    print(t , end = ' ')
    # trash.append(t)
    r = cards.rotate(-1)


    
