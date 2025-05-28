A,B = map(int,input().split())
a_list = []
b_list = []

for a in range(1,A+1):
    if A%a == 0:
        a_list.append(a)

for b in range(1 , B+1):
    if B%b == 0:
        b_list.append(b)

# 최대공약수(gcd) -> list에 공통된 값들 중 제일 큰 값
# 최소공배수(lcm) -> 두 수의 공통된 배수 중에서 가장 작은 값 

common = list(set(a_list) & set(b_list))
gcd = (max(common))
lcm = A * B / gcd
print(gcd)
print(int(lcm))

