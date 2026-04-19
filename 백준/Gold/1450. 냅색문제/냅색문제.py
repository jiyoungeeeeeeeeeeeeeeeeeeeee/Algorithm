import sys
from bisect import bisect_right

n,c = map(int,sys.stdin.readline().split())
weight = list(map(int,sys.stdin.readline().split()))
weight.sort()

cnt = 0
l = 0

left = weight[:n//2]
right = weight[n//2:]

left_sum = []
right_sum = []

def dfs(arr, idx, current_sum, result):
    if current_sum > c:
        return
    if idx == len(arr):
        result.append(current_sum)
        return

    dfs(arr, idx + 1, current_sum, result)
    dfs(arr, idx + 1, current_sum + arr[idx], result)


dfs(left, 0, 0, left_sum)
dfs(right, 0, 0, right_sum)

right_sum.sort()

count = 0

for s in left_sum:
    remain = c - s
    count += bisect_right(right_sum, remain)

print(count)
