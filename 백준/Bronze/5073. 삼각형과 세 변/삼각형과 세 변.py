tri = []

while True:
    a,b,c = (map(int,input().split()))
    if a+b+c == 0 :
        break

    tri.append([a,b,c])

for a,b,c in tri:
    max_side = max(a,b,c)
    total = a+b+c

    if max_side >= total - max_side:
        print('Invalid')
    
    else:
        if a==b==c:
            print('Equilateral')
        elif len(set([a,b,c])) == 2:
            print('Isosceles')
        else:
            print('Scalene')