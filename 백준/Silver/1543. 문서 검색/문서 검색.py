import sys

doc = sys.stdin.readline().strip()
word = sys.stdin.readline().strip()

c = doc.count(word)
print(c)