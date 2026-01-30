import sys

n = int(sys.stdin.readline())
assign = []
score = [0] * 1001

for _ in range(n):
    d,w = map(int,sys.stdin.readline().split())
    assign.append((d,w))

assign.sort(key = lambda x : -x[1])

for a,b in assign:
    if score[a] == 0:
        score[a] = b
    else:
        while a >= 1 :
            if score[a] == 0:
                score[a] = b
                break
            a -= 1

print(sum(score))


