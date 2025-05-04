n = int(input())

for i in range(n):
    total = i + sum(map(int,str(i)))

    if total == n :
        print(i)
        break
    
else :
    print(0)