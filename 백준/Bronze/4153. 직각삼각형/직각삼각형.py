import math

while True :
    a,b,c = list(map(int,input().split()))
    if a+b+c == 0:
        break

    s = sorted([a,b,c])

    if pow(s[2],2) == pow(s[0],2) + pow(s[1] ,2):
        print('right')
    else:
        print('wrong')
