n,m = map(int,input().split())

text_set = set()

for _ in range(n):
    text = input().strip()
    text_set.add(text)

cnt = 0
for _ in range(m):
    inspect = input().strip()

    if inspect in text_set:
        cnt += 1

print(cnt)