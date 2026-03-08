import sys

word = sys.stdin.readline().strip()

answers = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]

        new_word = a[::-1] + b[::-1] + c[::-1]
        answers.append(new_word)

print(min(answers))