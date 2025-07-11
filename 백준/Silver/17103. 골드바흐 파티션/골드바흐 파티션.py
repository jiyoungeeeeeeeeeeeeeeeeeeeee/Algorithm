import sys , math
T = int(sys.stdin.readline())

MAX = 1_000_000
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False


for i in range(2, int(math.sqrt(MAX))+ 1):
    if is_prime[i]:
        for j in range(i*i , MAX+1 , i):
            is_prime[j] = False


n_list = [int(input()) for _ in range(T)]
output = []

for n in n_list:
    cnt = 0
    for p in range(2, n // 2 + 1):
        if is_prime[p] and is_prime[n-p]:
            cnt += 1
    output.append(str(cnt))

print('\n'.join(output))