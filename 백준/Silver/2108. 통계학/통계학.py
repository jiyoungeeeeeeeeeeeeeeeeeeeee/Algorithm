import sys
from collections import Counter

n = int(sys.stdin.readline()) # 홀수

nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

cnt = Counter(nums)
nums.sort()
total = sum(nums)

avg = total / len(nums)
if avg > 0:
    print(int(avg + 0.5))
else:
    print(int(avg - 0.5))

print(nums[(n//2)])

vlst = []
for value in cnt.values():
    vlst.append(value)

max_freq = max(vlst)

modes =[]
for key,value in cnt.items():
    if value == max_freq:
        modes.append(key)
modes.sort()
if len(modes) >= 2:
    print(modes[1])
else:
    print(modes[0])

print(max(nums) - min(nums))
