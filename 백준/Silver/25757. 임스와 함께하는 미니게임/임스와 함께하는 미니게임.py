import sys

n,m = sys.stdin.readline().split()

newbie = set()

for _ in range(int(n)):
    player = sys.stdin.readline().strip()
    newbie.add(player)

    
if m == 'Y':
    print(len(newbie))

elif m == 'F':
    print(len(newbie)//2)

elif m == 'O':
    print(len(newbie)//3)     
