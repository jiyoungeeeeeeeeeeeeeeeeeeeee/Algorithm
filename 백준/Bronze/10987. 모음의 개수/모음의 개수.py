import sys

word = list(sys.stdin.readline().strip())
cnt = 0
vowel = ['a','e','i','o','u'] 

for w in word:
    if w in vowel:
        cnt += 1

print(cnt)

