import sys
n = int(sys.stdin.readline())
label = list(map(int,sys.stdin.readline().split()))

for l in label:
    if l == 300:
        print(1 , end = ' ')
    elif l >= 275 and l < 300:
        print(2 , end = ' ')
    elif l >= 250 and l < 275:
        print(3 , end = ' ')
    elif l < 250:
        print(4 , end = ' ')