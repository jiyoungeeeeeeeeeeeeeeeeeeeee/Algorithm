import sys

digit = list(sys.stdin.readline().split())
a,b = sys.stdin.readline().split()

def x (n):
    n = str(n)
    N = ''

    for i in n:
        d = digit.index(i)
        N += str(d)
    return int(N)

AB = x(a) + x(b)

def X (k):
    k = str(k)
    result = ''
    for j in k:
        D = digit[int(j)]
        result += D
    return result


print(X(AB))