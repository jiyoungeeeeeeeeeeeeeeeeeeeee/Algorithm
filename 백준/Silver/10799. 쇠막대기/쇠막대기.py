import sys
parentheses = list(sys.stdin.readline().rstrip())
result = 0
stack = []

for i in range(len(parentheses)):
    if parentheses[i] == "(":
        stack.append('(')
    else: #parentheses[i] = ')'
        stack.pop()
        if parentheses[i-1] =='(': # 레이저
            result += len(stack)
        else:
            result += 1
print(result)