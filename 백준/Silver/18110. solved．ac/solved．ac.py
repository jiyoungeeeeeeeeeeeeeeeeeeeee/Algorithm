import sys

n = int(sys.stdin.readline())

if n == 0:
    print(0)
    exit()

opi = []

for _ in range(n):
    opi.append(int(sys.stdin.readline()))
opi.sort()

drop = int(n*0.15 + 0.5)
trimmed = opi[drop:n-drop]
total = sum(trimmed)
individual = n - (2*drop)

avg = total / individual 

if avg >= 0:
    print(int(avg + 0.5))
else:
    print(int(avg - 0.5))
