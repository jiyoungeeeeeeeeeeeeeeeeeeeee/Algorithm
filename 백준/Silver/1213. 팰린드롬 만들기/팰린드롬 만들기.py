import sys
from collections import Counter

name = list(sys.stdin.readline().strip())
lengh = len(name)
c = Counter(name)

even = []
odd = []
mid = ''
left = ''

for key,value in c.items():
    if value %2 == 0:
        even.append((key,value))
    else:
        odd.append((key,value))

even.sort()
odd.sort()


if lengh % 2 == 0:
    if len(odd) != 0:
        print(f"I'm Sorry Hansoo")
        sys.exit(0)
    else:
        for k in sorted(c):
            left += (c[k]//2)*k


else:
    if len(odd) >= 2:
        print(f"I'm Sorry Hansoo")
        sys.exit(0)        
    else:
        mid = odd[0][0]

        for k in sorted(c):
                left += (c[k]//2)*k

print(left+mid+left[::-1])
