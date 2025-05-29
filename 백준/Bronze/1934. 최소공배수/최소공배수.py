import sys

T = int(sys.stdin.readline())

for t in range(T):
    a,b = map(int,sys.stdin.readline().split())

# 최소공배수 = a*b/최대공약수 

    A = []
    B = []

    for i in range(1,a+1):
        if a%i == 0:
            A.append(i)

    for j in range(1,b+1):
        if b%j == 0:
            B.append(j)

    gcd = max(set(A) & set(B))
    
    lcm = a*b/gcd
    print(int(lcm))