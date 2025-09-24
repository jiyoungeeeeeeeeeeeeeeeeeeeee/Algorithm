from itertools import permutations
n = int(input())
k = int(input())

num = []
for i in range(n):
    card = input().strip()
    num.append(card)

ans = set()
for p in permutations(num,k):
    ans.add(''.join(p))

print(len(ans))