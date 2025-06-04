import math
t = int(input())

for _ in range(t):
    nums = list(map(int,input().split()))
    total = 0
    for i in range(1,nums[0]):
        for j in range( i+1, len(nums)):
            g = math.gcd(nums[i],nums[j])
            total += g
    print(total)


