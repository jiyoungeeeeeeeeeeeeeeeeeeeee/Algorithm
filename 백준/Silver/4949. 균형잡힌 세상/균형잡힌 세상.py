lines = []
while True:
    text = input().rstrip()
    if text == '.':    
        break
    lines.append(text)

for line in lines:
    stack = []
    true = True

    for ch in line:
        if ch == "(" or ch == "[":
            stack.append(ch)     

        elif ch == ")":
            if not stack or stack[-1] != "(":
                true = False
                break

            stack.pop()
    
        elif ch == ']':
            if not stack or stack[-1] != '[':
                true = False
                break
            stack.pop()
 
    if true and not stack:
        print('yes')
    else:
        print('no')
