import sys
from collections import Counter

dic  = dict()
total = 0

while True:
    tree = sys.stdin.readline().strip()

    if not tree :
        break

    total += 1
    if tree not in dic:
        dic[tree] = 1
    else:
        dic[tree] += 1

t = list(dic.items()) 
t.sort()

for a,b in t:
    print(a,f"{b/total*100:.4f}")