import sys
n, m = map(int, sys.stdin.readline().split())

# 2의 개수 세기
two_n = 0
two_m = 0
two_nm = 0

k = 2
while k <= n:
    two_n += n // k
    k *= 2

k = 2
while k <= m:
    two_m += m // k
    k *= 2

k = 2
while k <= (n - m):
    two_nm += (n - m) // k
    k *= 2

# 5의 개수 세기
five_n = 0
five_m = 0
five_nm = 0

k = 5
while k <= n:
    five_n += n // k
    k *= 5

k = 5
while k <= m:
    five_m += m // k
    k *= 5

k = 5
while k <= (n - m):
    five_nm += (n - m) // k
    k *= 5

# 각각 조합 공식 적용해서 개수 빼기
total_two = two_n - two_m - two_nm
total_five = five_n - five_m - five_nm

# 10은 2와 5 한 쌍이므로 더 적은 쪽이 0의 개수
print(min(total_two, total_five))
