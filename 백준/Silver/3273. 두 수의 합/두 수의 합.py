import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
x = int(sys.stdin.readline())
arr.sort()

r = n-1
l = 0
cnt = 0


while l < r:
    sum_lr = arr[l] + arr[r]
    
    if sum_lr == x:
        cnt += 1
        r -= 1
        l += 1
    elif sum_lr > x:
        r -= 1
    elif sum_lr < x:
        l += 1

print(cnt)  

