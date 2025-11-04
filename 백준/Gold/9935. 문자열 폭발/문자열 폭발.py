text = input().strip()
boom = input().strip()
m = len(boom)
stack = []

for t in text:
    stack.append(t)
    
    if len(stack) >= m and ''.join(stack[-m:]) == boom:
        del stack[-m:]

print(''.join(stack) or "FRULA")
