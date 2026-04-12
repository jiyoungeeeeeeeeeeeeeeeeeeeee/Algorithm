import sys

n = int(sys.stdin.readline())
road = list(map(int,sys.stdin.readline().split()))
price = list(map(int,sys.stdin.readline().split()))

min_price = price[0]
total = min_price * road[0]

for i in range(1, n-1):
    if price[i] < min_price:
        min_price = price[i]
        
    total += min_price * road[i]

print(total)
