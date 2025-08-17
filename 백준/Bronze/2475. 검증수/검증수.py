import math
num = list(map(int,input().split()))
square = []

for n in num:
    square.append(pow(n,2))

Unique_number = (sum(square))%10
print(Unique_number)
