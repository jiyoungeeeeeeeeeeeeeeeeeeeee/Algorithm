import sys

S = sys.stdin.readline().strip()
k = []
y = []

for s in S:
    if not k and s =='K':
        k.append('K')
    if len(k) == 1 and s == 'O':
        k.append('O')
    if len(k) == 2 and s == 'R':
        k.append('R')
    if len(k) == 3 and s == 'E':
        k.append('E')
    if len(k) == 4 and s == 'A':
        k.append('A')


    if not y and s =='Y':
        y.append('Y')
    if len(y) == 1 and s == 'O':
        y.append('O')
    if len(y) == 2 and s == 'N':
        y.append('N')
    if len(y) == 3 and s == 'S':
        y.append('S')
    if len(y) == 4 and s == 'E':
        y.append('E')
    if len(y) == 5 and s == 'I':
        y.append('I')


    if len(k)>= len(y) and len(k) == 5:
        print(*k , sep='')
        
    if len(k) <= 4 and len(y) == 6:
        print(*y , sep='')
        break

        
   