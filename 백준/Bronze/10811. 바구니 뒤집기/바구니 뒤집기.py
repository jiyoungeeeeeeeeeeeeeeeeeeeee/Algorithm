n,m = map(int,input().split())

basket = [i for i in range(1, n+1)]
revers =[list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    start = revers[i][0] - 1
    end = revers[i][1]
    basket[start:end] = basket[start:end][::-1]

print(*basket)
        