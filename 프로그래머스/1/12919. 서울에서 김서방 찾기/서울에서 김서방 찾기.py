def solution(seoul):
    answer = '김서방은 '
    answer2 = '에 있다'
    dic = {}
    for i in range(len(seoul)):
        dic[seoul[i]] = i
        
    return answer + str(dic['Kim']) + answer2