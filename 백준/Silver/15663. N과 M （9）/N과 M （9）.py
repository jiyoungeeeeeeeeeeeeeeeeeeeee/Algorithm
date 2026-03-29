import sys

n,m = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
result = []
visited = [False] * n

def form():
    if len(result) == m:
        print(*result)
        return

    prev = 0

    for i in range(n):
        if visited[i] == False and prev != nums[i]:
            visited[i] = True
            result.append(nums[i])
            prev = nums[i]

            form()

            result.pop()
            visited[i] = False
form()