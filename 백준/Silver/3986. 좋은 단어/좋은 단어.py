import sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(n):
    good = []
    word = sys.stdin.readline().strip()

    for w in word:
        if not good :
            good.append(w)
        
        else:
            if good[-1] == w:
                good.pop()
            else:
                good.append(w)

    if not good:
        cnt += 1

print(cnt)