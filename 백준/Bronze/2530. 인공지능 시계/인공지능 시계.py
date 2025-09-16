a,b,c = map(int,input().split())
d = int(input())

c = c+d

while c >= 60:
    c = c-60
    b += 1

while b >= 60:
    b = b - 60
    a += 1

a %= 24

print(a , b, c)