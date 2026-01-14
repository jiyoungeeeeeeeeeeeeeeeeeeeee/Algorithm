import sys

n,s = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

length = []
l = 0
r = 0
current_sum = 0
cnt = 0

while True :
    
    if current_sum < s:
        if r==n:
            break
        current_sum += arr[r]
        r += 1
        

    while current_sum >= s:
        length.append(r-l)

        current_sum -= arr[l]
        l += 1

if length :
    print(min(length))
else:
    print(0)
        
        