import sys

n = int(sys.stdin.readline())

for i in range(n):
    lst = sys.stdin.readline().split()
    a = list(lst[0])
    b = list(lst[1])
    a.sort()
    b.sort()

    if a == b:  
        print('Possible')
    else:
        print('Impossible')