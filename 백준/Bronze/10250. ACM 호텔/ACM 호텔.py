import sys

T = int(sys.stdin.readline())

for t in range(T):
    h,w,n = map(int,sys.stdin.readline().split())
    
    floor = (n-1) % h + 1
    room  = (n-1) // h + 1

    print(floor * 100 + room)   