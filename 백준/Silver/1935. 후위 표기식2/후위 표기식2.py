n = int(input())
rpn = input()
stack = []
num = [int(input()) for _ in range(n)]

for r in rpn:
    if r.isalpha():
        index = ord(r) - ord("A")
        stack.append(num[index])
    else:
        b = stack.pop()
        a = stack.pop()

        if r == "+":
            stack.append(a+b)
        elif r == '-':
            stack.append(a-b)
        elif r == '/':
            stack.append(a/b)
        elif r == '*':
            stack.append(a*b)

print(f"{stack[0]:.2f}")