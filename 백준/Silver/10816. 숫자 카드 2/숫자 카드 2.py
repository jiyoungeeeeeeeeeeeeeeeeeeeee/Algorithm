import sys
from collections import Counter


n = int(sys.stdin.readline())
sang_card = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
has_card = list(map(int,sys.stdin.readline().split()))

dic = dict(Counter(sang_card))

for num in has_card:
    print(dic.get(num,0) , end = ' ')

