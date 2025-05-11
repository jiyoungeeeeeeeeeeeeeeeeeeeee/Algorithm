i = 1
n = int(input())
stack = []
result = []
is_possible = True

for _ in range(n):
    num = int(input())
    while i <= num:
        stack.append(i)
        result.append('+')
        i += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')

    else:
        is_possible = False 
        break

if is_possible:
    print('\n'.join(result) )

else :
    print('NO')