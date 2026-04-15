import sys

n = int(sys.stdin.readline())
arr1 = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False

for x in arr2:
    print(1 if binary_search(arr1, x) else 0)
