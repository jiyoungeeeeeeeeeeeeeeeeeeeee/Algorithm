import sys

MOD = 1000000007

def mul(A, B):
    result = [[0, 0], [0, 0]]

    result[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD
    result[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
    result[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD
    result[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD

    return result

def power(A, n):
    if n == 1:
        return A

    half = power(A, n // 2)
    half_squared = mul(half, half)

    if n % 2 == 0:
        return half_squared
    else:
        return mul(half_squared, A)

n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    base = [[1, 1], [1, 0]]
    answer = power(base, n)
    print(answer[0][1])