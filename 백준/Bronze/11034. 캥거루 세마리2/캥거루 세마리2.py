import sys

while True :
    k = list(map(int,sys.stdin.readline().split()))

    if not k:
        break
    
    l1 = abs(k[0] - k[1])
    l2 = abs(k[2] - k[1])

    print(max(l1,l2) - 1)