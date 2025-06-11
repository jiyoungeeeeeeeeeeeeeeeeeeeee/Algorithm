a, b = map(int, input().split())  # 진법 종류
M = int(input())                  # a진법 자릿수 개수
m = list(map(int, input().split()))  # a진법 자릿수들 (왼쪽부터 높은 자리)

# A진법 → 10진법으로 변환
ten = 0
for idx in range(M):
    ten += m[idx] * (a ** (M - 1 - idx))

# 10진법 → B진법으로 변환
save = []
if ten == 0:
    save.append(0)
else:
    while ten > 0:
        save.append(ten % b)
        ten //= b

print(*save[::-1])
