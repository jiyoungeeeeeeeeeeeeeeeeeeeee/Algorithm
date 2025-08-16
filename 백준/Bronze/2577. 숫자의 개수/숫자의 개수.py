a = int(input())
b = int(input())
c = int(input())

multiply = list(str(a * b * c))

for i in range(10):
    print(multiply.count(str(i)))