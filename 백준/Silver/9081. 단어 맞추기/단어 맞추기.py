import sys

for _ in range(int(sys.stdin.readline())):
    s = list(sys.stdin.readline().strip())
    i = len(s) - 2

    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1

    if i >= 0:
        j = len(s) - 1
        while s[j] <= s[i]:
            j -= 1
        s[i], s[j] = s[j], s[i]
        s[i + 1:] = s[i + 1:][::-1]

    print(''.join(s))