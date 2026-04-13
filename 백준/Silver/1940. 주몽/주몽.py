import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
num.sort()

l = 0
r = len(num) - 1
cnt = 0

while l < r:
    c = num[l] + num[r]

    if c > m:
        r -= 1
    elif c < m:
        l += 1
    else:
        cnt += 1
        l += 1
        r -= 1

print(cnt)