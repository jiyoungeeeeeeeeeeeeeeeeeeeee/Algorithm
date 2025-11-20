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
avg = int(sum(trimmed) / len(trimmed) + 0.5)

print(avg)
