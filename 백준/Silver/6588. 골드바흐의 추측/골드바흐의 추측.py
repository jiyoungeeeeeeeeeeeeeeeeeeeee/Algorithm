import sys
import math
input = sys.stdin.readline

MAX = 1_000_000
number = [False, False] + [True] * (MAX-1)
for i in range(2, int(MAX**0.5) + 1):
    if number[i]:
        number[i*i : MAX+1 : i] = [False] * (((MAX - i*i)//i) + 1)

primes = [i for i, is_p in enumerate(number) if is_p]

while True:
    n = int(input())
    if n == 0:
        break

    for p in primes:
        if p > n // 2:
            print("Goldbach's conjecture is wrong.")
            break
        if number[n - p]:
            print(f"{n} = {p} + {n-p}")
            break
