T = int(input())
# vps = [[input()] for _ in range(T)]


for _ in range(T):
    vps = input()
    stack = []
    is_valid = True

    for char in vps:
        if char == "(":
            stack.append(char)
        if char == ')':
            if stack:
                stack.pop()
            else:
                is_valid = False
                break
    
    if stack:
        is_valid = False
    print('YES' if is_valid else 'NO')