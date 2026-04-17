import sys

n = int(sys.stdin.readline())

if n == 1:
    print(0)
    sys.exit()

is_prime = [True] * (n + 1)
is_prime[0] = False
is_prime[1] = False

i = 2
while i * i <= n:
    if is_prime[i]:
        j = i * i
        while j <= n:
            is_prime[j] = False
            j += i
    i += 1

primes = []
i = 2
while i <= n:
    if is_prime[i]:
        primes.append(i)
    i += 1

l = 0
r = 0
total = 0
cnt = 0

while True:
    if total >= n:
        if total == n:
            cnt += 1
        total -= primes[l]
        l += 1
    else:
        if r == len(primes):
            break
        total += primes[r]
        r += 1

print(cnt)