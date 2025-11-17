import sys

formula = sys.stdin.readline().strip().split('-')
slst = []

for f in formula:
    part = f.split('+')
    s = 0

    for p in part:
        s += int(p)
    slst.append(s)

result = 0
for i in range(len(slst)):
    if i >= 1:
        result -= int(slst[i])
    else:
        result = result + int(slst[0])
print(result)

