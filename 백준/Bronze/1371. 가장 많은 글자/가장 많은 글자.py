import sys
from collections import Counter
c = Counter()
while True:
    text = sys.stdin.readline()
    if text == '':
        break
    text = text.strip()
    text = text.replace(' ','')

    c += Counter(text)

cc = sorted(c.items(), key = lambda x:(-x[1],x[0]))
result = []
maxx = cc[0][1]

for k,v in cc:
    if v == maxx:
        result.append(k)

print(''.join(result))
    