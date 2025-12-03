import sys

bowl = sys.stdin.readline().strip()
cnt = 0

for i in range(1 , len(bowl)):
    if bowl[i] == bowl[i-1]:
        cnt += 5
    else :
        cnt += 10

print(cnt + 10)
