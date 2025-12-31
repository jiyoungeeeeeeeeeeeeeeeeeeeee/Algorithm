import sys

n = int(sys.stdin.readline())
nums = []

for i in range(n):
    num = sys.stdin.readline().strip()
    a = 0
    for n in num:
        if n.isnumeric():
            a += int(n)
    
    nums.append((len(num),a,num))
nums.sort()

for a,b,c in nums:
    print(c)
    