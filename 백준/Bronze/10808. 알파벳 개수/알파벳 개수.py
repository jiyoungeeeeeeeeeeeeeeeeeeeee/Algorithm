s = input()

# num을 인덱스로 활용
zero = [ 0 for i in range(26)]

for i in s:
    num = ord(i) - ord('a')
    zero[num] += 1
print(*zero)