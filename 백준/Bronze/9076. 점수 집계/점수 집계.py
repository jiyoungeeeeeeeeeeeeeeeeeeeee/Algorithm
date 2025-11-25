import sys

T = int(sys.stdin.readline())
for t in range(T):
    scores = list(map(int,sys.stdin.readline().split()))
    MAX = max(scores)
    MIN = min(scores)

    scores.remove(MAX)
    scores.remove(MIN)

    scores.sort()

    if scores[2] - scores[0] >= 4:
        print('KIN')
    else:
        print(sum(scores))