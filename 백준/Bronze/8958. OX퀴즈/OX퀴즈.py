t = int(input())

for _ in range(t):
    quiz = input()
    stack = []
    cnt = 0

    for q in quiz:
        if q == "O":
            cnt += 1
            stack.append(cnt) 
        elif q == "X":
            cnt = 0
            stack.append(cnt)
    print(sum(stack))

                