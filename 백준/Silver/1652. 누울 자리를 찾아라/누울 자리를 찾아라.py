import sys

n = int(sys.stdin.readline())
row = 0
col = 0
total = []

for _ in range(n):
    room = sys.stdin.readline().rstrip()
    lr = list(room)
    total.append(lr)

    rroom = room.split('X')

    for r in rroom:
        if r == '':
            pass
        else:
            if len(r) >= 2:
                row += 1

for i in range(n):
    strr = ''
    for j in range(n):
        strr += total[j][i]

    croom = strr.split('X')

    for c in croom:
        if c == '':
            pass
        else:
            if len(c) >= 2:
                col += 1
print(row ,col)