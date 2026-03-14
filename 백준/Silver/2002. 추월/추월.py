import sys

n = int(sys.stdin.readline())
inputt = {}
output = []
for i in range(n):
    a = sys.stdin.readline().strip()
    inputt[a] = i

for _ in range(n):
    b = sys.stdin.readline().strip()
    output.append(inputt[b])


cnt = 0

for i in range(n):
    for j in range(i + 1, n):
        if output[i] > output[j]:
            cnt += 1
            break

print(cnt)
