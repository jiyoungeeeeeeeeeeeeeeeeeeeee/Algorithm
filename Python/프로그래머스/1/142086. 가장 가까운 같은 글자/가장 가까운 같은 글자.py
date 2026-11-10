def solution(s):
    dic = {}
    answer = []
    
    for idx,string in enumerate(s) :
        if string in dic:
            cnt = idx - dic[string]
            answer.append(cnt)
            dic[string] = idx
        else:
            dic[string] = idx
            answer.append(-1)
    
    return answer