L = int(input())
alpa = input()
result = 0
trans_num = []

for A in alpa:
    s = ord(A) - ord('a') + 1
    trans_num.append(s)

for i in range(L):
    result += trans_num[i] * (31**i)
print(result)