import sys
from collections import Counter

n = int(sys.stdin.readline())
lst = []
sett = set()

for _ in range(n):
    word = sys.stdin.readline().strip()
    
    w = sorted(word)
    re = ''.join(w)
    sett.add(re)
print(len(sett))