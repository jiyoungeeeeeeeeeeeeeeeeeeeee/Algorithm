n = int(input())
result= 1
if n >= 1:
    for i in range(1, n+1):
        result *= i
    print(result)

else:
    print(1)