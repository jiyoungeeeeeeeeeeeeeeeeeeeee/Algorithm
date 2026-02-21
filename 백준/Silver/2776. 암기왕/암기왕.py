import sys

input = sys.stdin.readline

t = int(input())
out_lines = []

for _ in range(t):
    n = int(input())
    note1 = set(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    for x in note2:
        if x in note1:
            out_lines.append("1")
        else:
            out_lines.append("0")

sys.stdout.write("\n".join(out_lines))
