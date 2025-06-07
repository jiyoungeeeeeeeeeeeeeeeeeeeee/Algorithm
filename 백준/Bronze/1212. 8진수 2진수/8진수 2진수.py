import sys

octal = sys.stdin.readline().strip()

for i in range(len(octal)):
    o = octal[i]
    b = bin(int(o))[2:]
    if i == 0:
        print(b, end='')
    else:
        print(b.zfill(3), end='')
