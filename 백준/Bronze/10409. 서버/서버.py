import sys
n,t = map(int,sys.stdin.readline().split())

server = list(map(int,sys.stdin.readline().split()))
result = []
total = 0
cnt = 0


for i in range(n):
    if total >= t :
        break
    else:
        total += server[i]
        result.append(total)


for r in result:
    if r <= t:
        cnt += 1
    else:
        break
print(cnt)    