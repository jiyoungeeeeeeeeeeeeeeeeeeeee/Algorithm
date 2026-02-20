n = int(input())
ys = 100
ds = 100

for i in range(n):
    y,d = map(int,input().split())

    if y > d :
        ds = ds - y
    elif y < d :
        ys = ys - d
    elif y == d:
        continue

print(ys , ds , sep = '\n')