import sys

a,b = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
brr = list(map(int,sys.stdin.readline().split()))

arr = set(arr)
brr = set(brr)

result = sorted(arr - brr)

print(len(arr - brr))
print(*result)