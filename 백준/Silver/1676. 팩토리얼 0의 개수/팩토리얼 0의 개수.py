n = int(input())

result = 1
cnt = 0

if n >= 1:
    for i in range(1,n+1):
        result *= i

for r in reversed(str(result)):
    if r == '0':
        cnt += 1
    else:
        break
print(cnt)