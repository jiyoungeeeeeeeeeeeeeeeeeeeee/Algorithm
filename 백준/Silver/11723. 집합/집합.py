import sys
m = int(sys.stdin.readline())
s = []

for i in range(m):
    command = sys.stdin.readline().split()

    if command[0] == 'add':
        if command[1] in s:
            continue
        else:
            s.append(command[1])
    
    if command[0] == 'remove':
        if command[1] in s:
            s.remove(command[1])
        else:
            continue
    
    if command[0] == 'check':
        if command[1] in s:
            print(1 )
        else:
            print(0 )
    
    if command[0] == 'toggle':
        if command[1] in s:
            s.remove(command[1])
        else:
            s.append(command[1])
    
    if command[0] == 'all':
        s = [str(i) for i in range(1,21)]
    
    if command[0] == 'empty':
        s.clear()

