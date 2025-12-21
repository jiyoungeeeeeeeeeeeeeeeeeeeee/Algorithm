import sys
from collections import Counter

n = int(sys.stdin.readline())
recipe = sys.stdin.readline().rstrip('\n').split()
wrong = list(sys.stdin.readline().rstrip('\n').split())

rc = Counter(recipe)
wc = Counter(wrong)

print(*rc-wc)


    