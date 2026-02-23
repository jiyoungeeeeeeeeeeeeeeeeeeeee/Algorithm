import sys
from collections import Counter

n,m = map(int,sys.stdin.readline().split())
dna = []

for _ in range(n):
    DNA = sys.stdin.readline().strip()
    dna.append(DNA)

hd = ''
dist = 0

for i in range(m):
    save = []
    for j in range(n):
        save.append(dna[j][i])   
    c = Counter(save)

    cs = sorted(c.items() , key = lambda x: (-x[1], x[0]))
    hd += cs[0][0]
    dist += n - cs[0][1]
    

print(hd)
print(dist)

