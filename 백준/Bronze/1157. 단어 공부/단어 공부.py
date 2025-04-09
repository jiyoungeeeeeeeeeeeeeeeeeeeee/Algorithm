s = input().upper()
s_list = list(set(s))       # 중복 제거해서 한 번씩만 확인
s_cnt_list = []

for i in s_list:
    s_cnt = s.count(i)      # 중복 제거한 값(s_list) 말고 원래 값 count
    # print(s_cnt)          # 알파벳 빈도 수 count한 배열
    s_cnt_list.append(s_cnt)

# print(s_cnt_list)
max_value = max(s_cnt_list)   # 최댓값 출력
# print(max_value)            

#print(s_cnt_list.count(max_value))
if s_cnt_list.count(max_value) > 1:
    print('?')
else :
    max_index = s_cnt_list.index(max_value)   # 빈도 수 list에서 최댓값 인덱스를 찾은 후 반환
    print(s_list[max_index])                  # 