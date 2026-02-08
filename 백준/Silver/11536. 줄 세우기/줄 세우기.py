import sys

n = int(sys.stdin.readline())
first = []
for i in range(n):
    name = sys.stdin.readline().strip()
    first.append(name)

valid1 = sorted(first)


if valid1 == first:
    print('INCREASING')
elif valid1[::-1] == first:
    print('DECREASING')
else:
    print('NEITHER')