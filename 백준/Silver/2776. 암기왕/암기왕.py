import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    note1 = set(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    note2 = list(map(int,sys.stdin.readline().split()))

    result = []

    for i in note2:
        if i in note1:
            result.append('1')
        else:
            result.append('0')

    sys.stdout.write("\n".join(result) + "\n")
