while True:
    a,b,c = sorted(list(map(int,input().split())))
    if a+b+c == 0:
        break
    
    if c >= a+b :
        print('Invalid')
    
    else :
        if a==b==c :
            print('Equilateral')
        if a != b and a != c and b != c:
            print('Scalene')
        if ( a == b  or b == c ) and a != c :
            print('Isosceles')
