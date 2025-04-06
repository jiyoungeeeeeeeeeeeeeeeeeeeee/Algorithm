nums = [int(input()) for _ in range(9)]

max_val = max(nums)
max_index = nums.index(max_val)

print(max_val)
print(max_index+1)