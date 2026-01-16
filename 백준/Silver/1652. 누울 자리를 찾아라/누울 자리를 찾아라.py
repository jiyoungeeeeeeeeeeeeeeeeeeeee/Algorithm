import sys

n = int(sys.stdin.readline())
row = 0
col = 0
total = []

def Room(rooms): 
    cnt = 0
    for r in rooms:
        if len(r) >= 2:
            cnt += 1
    return cnt

for _ in range(n):
    room = sys.stdin.readline().rstrip()
    lr = list(room)
    total.append(lr)
    row += Room(room.split('X'))
    

for i in range(n):
    strr = ''
    for j in range(n):
        strr += total[j][i]
    col += Room(strr.split('X'))

print(row ,col)

