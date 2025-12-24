import sys

board = sys.stdin.readline().strip().split('.')
answer = []

for d in board:
    if d != '':
        if len(d) % 2 != 0:
            print(-1)
            sys.exit(0)
        else:
                a = len(d)//4
                b = len(d)%4
                answer.append(a*'AAAA'+(b//2)*"BB")
          
    else:
        answer.append('')

print('.'.join(answer))
