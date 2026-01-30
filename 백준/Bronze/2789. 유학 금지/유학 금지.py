import sys

word = sys.stdin.readline().strip()
sensor = 'CAMBRIDGE'

for w in word:
    if w in sensor:
        pass
    else:
        print(w , end = '')