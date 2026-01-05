import sys

s = sys.stdin.readline().strip()

zero = s.split('0')
one  = s.split('1')

znt = 0
ont = 0

for z in zero:
    if z != '':
        znt += 1

for o in one:
    if o != '':
        ont += 1
   

print(min(znt , ont))
