n = int(input())
arr = [list(map(int,input().split()))]
v = int(input())
cnt = 0

for i in range(n):
    for a in arr:
        if a[i] == v:
            cnt += 1
print(cnt)
 