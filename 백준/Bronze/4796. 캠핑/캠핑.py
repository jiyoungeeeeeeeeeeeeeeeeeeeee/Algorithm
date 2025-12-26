import sys

num = 1

while True:
    arr = list(map(int,sys.stdin.readline().split()))
    if sum(arr) == 0:
        break
    l,p,v = arr[0],arr[1],arr[2]
    result = int(v//p * l + min(v%p,l))  

    print(f"Case {num}: {result}")
    num += 1