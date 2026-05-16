def solution(name, yearning, photo):
    answer = []
    dic = {}
    
    for i in range(len(name)):
        dic[name[i]] = yearning[i]

        
    for p in photo:
        s = 0
        
        for h in p:
            if h in dic:
                s += dic.get(h,0)
    
        answer.append(s)            
    
    return answer