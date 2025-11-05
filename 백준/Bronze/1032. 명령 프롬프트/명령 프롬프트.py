n = int(input())

lst = []
cnt = 0

for _ in range(n):
    name = input().strip()
    lst.append(name)
    cnt = len(name)

result = []
for i in range(cnt):
    same = True
    for j in range(1,n):
        if lst[j][i] != lst[0][i]:
            same = False
            break
    if same:
        result.append(lst[0][i])
    else:
        result.append('?')

print(''.join(result))
