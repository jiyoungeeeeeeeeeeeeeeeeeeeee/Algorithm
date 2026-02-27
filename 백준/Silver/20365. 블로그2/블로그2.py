import sys

n = int(sys.stdin.readline())
blog = sys.stdin.readline().strip()

b = blog.count('B')
r = blog.count('R')

cnt = 0

for i in range(n-1):
    if blog[i] != blog[i+1]:
        cnt += 1

print(1+ (cnt + 1) // 2)        