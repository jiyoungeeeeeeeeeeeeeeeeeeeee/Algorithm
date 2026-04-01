import sys

digit = list(sys.stdin.readline().split())
a,b = sys.stdin.readline().split()
to_idx = dict()

for t in range(10):
    to_idx[digit[t]] = str(t)

def x (n):
    n = str(n)
    N = ''

    for i in n:
        N += to_idx[i]
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