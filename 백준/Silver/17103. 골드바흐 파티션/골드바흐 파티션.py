import sys
input = sys.stdin.readline

T = int(input())
Ns = [int(input()) for _ in range(T)]
maxN = max(Ns)

# 1) 최대 N까지 한 번만 에라토스테네스의 체로 소수 여부 계산
is_prime = [True] * (maxN + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(maxN**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, maxN + 1, i):
            is_prime[j] = False

# 2) 각 테스트 케이스마다 골드바흐 파티션 개수 세기
for N in Ns:
    cnt = 0
    # p ≤ N//2 까지만 검사하면 (p, N-p) 쌍의 중복을 막을 수 있어
    for p in range(2, N//2 + 1):
        if is_prime[p] and is_prime[N - p]:
            cnt += 1
    print(cnt)
