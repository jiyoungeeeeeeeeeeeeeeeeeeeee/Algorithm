import sys
m = int(sys.stdin.readline())
s = [0] * 21
out = []


for i in range(m):
    command = sys.stdin.readline().split()
    
    if command[0] == 'add':
        x = int(command[1])
        s[x] = 1
    
    elif command[0] == 'remove':
        x = int(command[1])
        s[x] = 0
    
    elif command[0] == 'check':
        x = int(command[1])

        if s[x] == 1:
            print(1)
        else:
            print(0)
    
    elif command[0] == 'toggle':
        x = int(command[1])
        if s[x] == 1:
            s[x] = 0  
        else:
            s[x] = 1
    
    elif command[0] == 'all':
        s = [0] + [1] * 20
    
    elif command[0] == 'empty':
        s = [0]*21
