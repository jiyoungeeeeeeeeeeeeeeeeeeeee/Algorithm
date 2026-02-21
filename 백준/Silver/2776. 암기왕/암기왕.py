import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    note1 = set(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    note2 = list(map(int,sys.stdin.readline().split()))

    
    for o in note2:
        if o in note1:
            print(1)
        else:
            print(0)    
