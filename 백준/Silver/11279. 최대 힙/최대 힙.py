import heapq , sys

n = int(sys.stdin.readline())
heaq = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(heaq,-x)
    
    else:
        if heaq:
            print(-heapq.heappop(heaq))
        else:
            print(0)
