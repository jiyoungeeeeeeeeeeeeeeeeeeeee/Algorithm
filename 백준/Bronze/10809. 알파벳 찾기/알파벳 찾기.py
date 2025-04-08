s = input()

result = [-1 for _ in range(26)]


for i in range(len(s)):
    index = ord(s[i])-ord('a')
    if result[index] == -1:
        result[index] = i

for r in result:
    print(r, end =' ') 
    