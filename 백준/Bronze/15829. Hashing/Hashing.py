L = int(input())
alpa = input()
result = 0
trans_num = []
MOD = 1234567891

for A in alpa:
    trans_num.append(ord(A) - ord('a') + 1)

p = 1  

for i in range(L):
    result = (result + trans_num[i] * p) % MOD
    p = (p * 31) % MOD
print(result)
