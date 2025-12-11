import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    com = list(map(int,sys.stdin.readline().split()))
    command = com[0]

    if command == 1:
        lst.append(com[1])
    
    elif command == 2:
        if lst:
            print(lst[-1])
            lst.pop()
        else:
            print(-1)
    elif command == 3:
        print(len(lst))
    elif command == 4:
        if lst:
            print(0)
        else:
            print(1)
    elif command == 5:
        if lst:
            print(lst[-1])
        else:
            print(-1)
