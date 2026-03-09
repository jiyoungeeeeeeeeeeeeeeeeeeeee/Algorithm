import sys

t = int(sys.stdin.readline())

for _ in range(t):
    word = list(sys.stdin.readline().strip())
    n = len(word)

    i = n - 2
    while i >= 0 and word[i] >= word[i + 1]:
        i -= 1

    if i == -1:
        print(''.join(word))
        continue

    j = n - 1
    while word[j] <= word[i]:
        j -= 1

    word[i], word[j] = word[j], word[i]
    word[i + 1:] = reversed(word[i + 1:])

    print(''.join(word))