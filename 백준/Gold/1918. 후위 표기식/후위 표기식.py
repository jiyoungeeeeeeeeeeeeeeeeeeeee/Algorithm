infix = input()
postfix = []    # 후위 표기식
oper = []       # 연산자
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0} # 연산자 우선순위 

for i in infix:
    if i.isalpha():         # 문자열일 경우
        postfix.append(i)
    else :                  # () 경우
        if i == "(":
            oper.append(i)
        elif i == ")":
            while oper and oper[-1] != "(":
                postfix.append(oper.pop())
            oper.pop() # ( 제거
        else:               # + - * /  경우
            while oper and priority[oper[-1]] >= priority[i]:
                postfix.append(oper.pop())
            oper.append(i)
while oper:
    postfix.append(oper.pop())

print(*postfix, sep='')
