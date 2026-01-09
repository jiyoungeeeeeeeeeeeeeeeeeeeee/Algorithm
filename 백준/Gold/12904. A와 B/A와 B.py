import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

cur = t

while len(cur) > len(s):
    if cur[-1] == 'A':
        cur = cur[:-1]
        pass
    elif cur[-1] == 'B':
        cur = cur[:-1]
        cur = cur[::-1]
        pass

if cur == s:
    print(1)
else:
    print(0)