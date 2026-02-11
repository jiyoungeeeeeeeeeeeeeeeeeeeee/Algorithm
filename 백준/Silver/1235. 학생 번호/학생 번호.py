import sys

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    nums = sys.stdin.readline().strip()
    lst.append(nums)
    s = len(nums)

answer = 0

for j in range(1,s+1):
    position = set()

    for i in range(n):
        part = lst[i][-j:]
        position.add(part[::-1])

    if len(position) == n:
        answer = j
        break

print(answer)
