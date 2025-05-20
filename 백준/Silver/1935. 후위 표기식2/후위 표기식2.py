n = int(input()) # 1부터 26까지 
RPN = input()    # 후위 표기식
values = {}
stack = []

# 후위 표기식의 문자열 -> 숫자로 변환
for i in range(n):
    values[chr(ord('A') + i)] = int(input()) 

# 연산자 / 피연산자 나눠서 스택에 저장
for token in RPN:
    if token.isalpha():
        stack.append(values[token])
    else:
        b = stack.pop() # i-2
        a = stack.pop() # i-1

        # 실제 계산은 i-2 -> i-1
        if token == "+":
            stack.append(a + b)
        elif token == '-':
            stack.append(a - b)
        elif token == '*':
            stack.append(a * b)
        elif token == '/':
            stack.append(a / b)


print(f"{stack[0]:.2f}")
