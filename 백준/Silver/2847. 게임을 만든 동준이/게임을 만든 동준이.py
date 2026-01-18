import sys

n = int(sys.stdin.readline())
scores = []
for _ in range(n):
    scores.append(int(sys.stdin.readline()))
cnt = 0
target = scores[-1]
i = n-2

while i >= 0:
    if scores[i] >= target:
        cnt += scores[i] - (target-1)
        scores[i] = target-1
        
    target = scores[i]
    i -= 1
print(cnt)