import sys

db , dt = sys.stdin.readline().split()
mb , mt = sys.stdin.readline().split()

color = []
color.extend([db, dt, mb, mt])

result = set()

for i in range(len(color)):
    for j in range(len(color)):
        result.add((color[i] , color[j]))
r = sorted(result)

for a,b in r:
    print(a,b)