import sys

text = sys.stdin.readline().strip()
stance = 0

start_diff = abs(ord(text[0]) - ord('A'))
start = min(start_diff, 26 - start_diff)

for i in range (1,len(text)):
    diff = abs(ord(text[i-1]) - ord(text[i]))
    stance += min(diff , 26-diff)

print(stance + start)

