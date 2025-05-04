n,m = map(int,input().split())
cards = list(map(int,input().split()))
cards_sum = 0
max_n = []

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            cards_sum = cards[i]+cards[j]+cards[k]
            if cards_sum > m:
                continue
            else:
                max_n.append(cards_sum)
print(max(max_n))

               