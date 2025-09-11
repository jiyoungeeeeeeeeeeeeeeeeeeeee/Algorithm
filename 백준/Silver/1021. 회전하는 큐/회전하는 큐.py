from collections import deque

n,m = map(int,input().split())
targets = list(map(int,input().split()))
dq = deque(range(1 , n+1)) 
moves = 0

for x in targets:
    pos = dq.index(x)
    left = pos 
    right = len(dq) - pos

    if left <= right :
        dq.rotate(-left)
        moves += left

    else:
        dq.rotate(right)
        moves += right
    
    dq.popleft()

print(moves)
