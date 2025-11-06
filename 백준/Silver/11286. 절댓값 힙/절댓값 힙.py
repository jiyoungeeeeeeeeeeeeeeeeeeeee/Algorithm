import heapq , sys

n = int(input())
heaq = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heaq,(abs(x) , x))
    else:
        if heaq:
            print(heapq.heappop(heaq)[1])
        else:
            print(0)
