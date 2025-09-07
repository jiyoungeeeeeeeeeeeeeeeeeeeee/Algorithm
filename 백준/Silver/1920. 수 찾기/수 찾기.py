import sys

n = int(input())
arr1 = set(map(int,sys.stdin.readline().split()))
m = int(input())
arr2 = list(map(int,sys.stdin.readline().split()))

for x in arr2:
    if x in arr1:
        print(1)
    else:
        print(0)