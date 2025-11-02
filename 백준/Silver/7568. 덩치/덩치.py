n = int(input())
people = []  

for _ in range(n):
    x, y = map(int, input().split())
    people.append((x, y))


for i in range(n):
    rank = 1  
    for j in range(n):
        if i != j:
            if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
                rank += 1
    print(rank, end=' ')
