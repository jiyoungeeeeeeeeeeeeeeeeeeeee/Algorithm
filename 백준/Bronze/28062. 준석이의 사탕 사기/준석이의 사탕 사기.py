import sys

n = int(sys.stdin.readline())
candy = list(map(int,sys.stdin.readline().split()))
even = []
odd = []

for i in candy:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
odd.sort(reverse = True)

if len(odd)%2 != 0:
    print(sum(even) + sum(odd[:-1]))
else:
    print(sum(even) + sum(odd))
        