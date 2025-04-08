s = input().lower() # 모두 소문자로 바꿔주기
cnt_index = {}

for i in range(len(s)):
    index = ord(s[i]) - ord('a')
    if index in cnt_index:
        cnt_index[index] += 1
    else : 
        cnt_index[index] = 1

max_count = max(cnt_index.values())
most_count = [k for k,v in cnt_index.items() if v == max_count]

if len(most_count) >=2:
    print('?')
else :
    print(chr(most_count[0] + ord('A')))