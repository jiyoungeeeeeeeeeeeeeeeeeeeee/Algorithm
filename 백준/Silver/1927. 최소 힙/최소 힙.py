import sys, heapq
n = int(sys.stdin.readline())

h=[]
out = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x:
        heapq.heappush(h, x)      
    else:
        out.append(str(heapq.heappop(h) if h else 0)) 

sys.stdout.write("\n".join(out))
 
