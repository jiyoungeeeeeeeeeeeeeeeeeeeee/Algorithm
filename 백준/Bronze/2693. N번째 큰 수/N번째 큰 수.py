import sys

T = int(sys.stdin.readline())

for t in range(T):
    arr = list(map(int,sys.stdin.readline().split()))

    arr.sort(reverse = True)
    print(arr[2])  