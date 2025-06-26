import sys

n = int(sys.stdin.readline())
count = [0] * 10001  

for _ in range(n):
    s = int(sys.stdin.readline())
    count[s] += 1
    
for i in range(1, 10001):
    for _ in range(count[i]):
        print(i)
