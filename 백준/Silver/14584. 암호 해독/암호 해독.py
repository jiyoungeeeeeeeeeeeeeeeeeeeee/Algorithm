import sys

cyper = sys.stdin.readline().strip()
n = int(sys.stdin.readline())

words = []
for _ in range(n):
    words.append(sys.stdin.readline().strip())

i = 0
while i < 26:
    out = []
    for ch in cyper:
        x = ord(ch) - ord('a')
        x = (x + i) % 26
        out.append(chr(ord('a') + x))
    decoded = ''.join(out)

    ok = False
    for word in words:
        if word in decoded:
            ok = True
            break
    if ok:
        print(decoded)
        break

    i += 1