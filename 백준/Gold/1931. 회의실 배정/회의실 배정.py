import sys

n = int(sys.stdin.readline())
meet = []
for _ in range(n):
    s,e = map(int,sys.stdin.readline().split())
    meet.append((s,e))
meet.sort(key = lambda x: (x[1],x[0]))

result = []
meeting = meet[0]
result.append(meeting)

for m in meet[1:]:
    if meeting[1] <= m[0]:
        result.append(m)
        meeting = m 
print(len(result))
        