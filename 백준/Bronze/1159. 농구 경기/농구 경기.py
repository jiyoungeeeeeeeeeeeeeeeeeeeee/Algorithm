import sys

n = int(sys.stdin.readline())

first = []

for _ in range(n):
    names = sys.stdin.readline().strip()
    first.append(names[0])

cnt = {}

for f in first:
    cnt[f] = cnt.get(f,0) + 1

result = []
for k,v in cnt.items():
    if v >= 5:
        result.append(k)

result.sort()
if result :
    print(*result , sep = '')
else:
    sys.stdout.write('PREDAJA')


