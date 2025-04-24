tri=[]

for i in range(3):
    angle = int(input())

    tri.append(angle)

if sum(tri) == 180:
    if min(tri) == max(tri):
        print('Equilateral')
    elif len(set(tri))== 2:
        print('Isosceles')
    else :
        print('Scalene')

else : 
    print('Error')
