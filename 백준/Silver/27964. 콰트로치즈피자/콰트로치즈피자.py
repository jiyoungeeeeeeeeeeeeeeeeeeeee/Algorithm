import sys

n = int(sys.stdin.readline())
topping = sys.stdin.readline().strip().split()
sett = set()

for t in topping:
    if t[-6:] == 'Cheese':
        sett.add(t)

if len(sett) >= 4:
    print('yummy')
else:
    print('sad')
