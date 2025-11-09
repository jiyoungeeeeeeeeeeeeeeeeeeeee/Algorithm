from collections import Counter
import sys
n,m = map(int,sys.stdin.readline().split())

words = []

for i in range(n):
    word = sys.stdin.readline().strip()
    line = len(word)

    if line >= m:
        words.append(word)
    else:
        continue

counter = Counter(words)
info = []

for w,cnt in counter.items():
    info.append((-cnt,-len(w),w))

info.sort()

result = []
for item in info:
    result.append(item[2])

sys.stdout.write("\n".join(result))
