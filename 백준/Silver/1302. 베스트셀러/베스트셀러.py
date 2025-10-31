n = int(input())
dicts = {}
best = []

for _ in range(n):
    title = input().strip()
    dicts[title] = dicts.get(title,0) + 1

best_cnt = max(dicts.values())

for key,value in dicts.items():
    if value == best_cnt:
        best.append(key)

best.sort()
print(best[0])


    