tri = []

while True:
    x,y,z = map(int,input().split())

    if x+y+x == 0:
        break    
    tri.append((x,y,z))

for x,y,z in tri:
    max_side = max(x,y,z)
    total = x+y+z
    
    if max_side >= total - max_side:
        print('Invalid')
    elif x == y == z:
        print('Equilateral')
    elif len(set((x,y,z))) == 2:
        print('Isosceles')
    else:
        print('Scalene')
