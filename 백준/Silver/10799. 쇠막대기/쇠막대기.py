import sys

parentheses = sys.stdin.readline().strip()
stack = []
cnt = 0

for p in range(len(parentheses)):
    if parentheses[p] == "(":
        stack.append(p)

    else:
        stack.pop()
        if parentheses[p-1] == "(" : # 레이저 
            cnt += len(stack)
        else: # 쇠막대기
            cnt += 1
print(cnt)
    