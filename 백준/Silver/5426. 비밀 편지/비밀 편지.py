import sys

n = int(sys.stdin.readline())

for _ in range(n):
    lst = []
    text = sys.stdin.readline().strip()
    r = int(len(text) ** 0.5)
    i = 0
    
    while i < r:
        lst.append(text[i::r])
        i += 1
    print(*lst[::-1] , sep = '' )