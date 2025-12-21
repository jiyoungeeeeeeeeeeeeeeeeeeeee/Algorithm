import sys

n = int(sys.stdin.readline())
sticks = []

for i in range(n):
    sticks.append(int(sys.stdin.readline().strip()))

max_height = 0
cnt = 0

for i in range(n-1,-1,-1):
    if sticks[i] > max_height :
        cnt += 1
        max_height = sticks[i]

print(cnt)
