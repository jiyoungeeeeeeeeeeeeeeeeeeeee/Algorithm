import sys
channel = int(sys.stdin.readline())
now = 100

prohibition = set() 
n = int(input())
if n:
    prohibition = set(map(int,input().split()))

sign = abs(channel - now)

allowed = {str(d) for d in range(10) if d not in prohibition}


for num in range(1_000_000):
    s = str(num)
    if all (ch in allowed for ch in s):
        presses = len(s) + abs(channel - num)
        if presses < sign:
            sign = presses
print(sign)
