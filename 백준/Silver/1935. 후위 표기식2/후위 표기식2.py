n = int(input())
RPN = input()
nums = [int(input()) for _ in range(n)]
stack = []

for token in RPN:
    if token.isalpha(): # 피연산자 일 경우
        index = ord(token)- ord("A")
        stack.append(nums[index]) 
    else: # 연산자일 경우
        b = stack.pop()
        a = stack.pop()

        if token == "+":
            stack.append(a+b)
        elif token == "*":
            stack.append(a*b)
        elif token == "/":
            stack.append(a/b)
        elif token == '-':
            stack.append(a-b)

print(f"{stack[0]:.2f}")
