T = int(input())

text = [(list(input(str()).split())) for _ in range(T)]


for i in range(T): #행
    for j in range(len(text[i])): #열
        text[i][j] = text[i][j][::-1]
    print(' '.join(text[i]))
