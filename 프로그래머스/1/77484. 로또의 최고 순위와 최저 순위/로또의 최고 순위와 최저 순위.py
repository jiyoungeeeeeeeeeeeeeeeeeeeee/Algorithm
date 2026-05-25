def solution(lottos, win_nums):
    answer = []
    dic = {6:1,5:2,4:3,3:4,2:5,1:6,0:6} # 맞춘 갯수 : 순위
    z = lottos.count(0)
    
    result = set(lottos) & set(win_nums)
    cnt = len(result)
    MAX = cnt + z
    MIN = cnt 
    
    a = dic.get(MAX)
    b = dic.get(MIN)
    
    answer.append(a)
    answer.append(b)
    
    return answer
    