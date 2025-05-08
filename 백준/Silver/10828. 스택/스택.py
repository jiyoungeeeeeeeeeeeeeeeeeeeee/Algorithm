import sys
n = int(sys.stdin.readline())

stack = []

for i in range(n):
    com = sys.stdin.readline()

    if 'push' in com:
        value = int(com.split()[1])
        stack.append(value)
    
    if 'pop' in com:
        if stack:
            print(stack[-1])
            stack.pop()
        elif not stack:
            print(-1)
    
    if 'size' in com:
        print(len(stack))
    
    if 'empty' in com:
        if not stack:
            print(1)
        if stack:
            print(0)

    if 'top' in com:
        if stack:
            print(stack[-1])
        if not stack:
            print(-1)
