import sys

n = int(sys.stdin.readline())
sang_card = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
has_card = list(map(int,sys.stdin.readline().split()))

for h in has_card:
    if h in sang_card:
        print(1 , end = ' ')
    else:
        print(0 , end = ' ')