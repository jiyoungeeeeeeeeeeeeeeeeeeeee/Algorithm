def solution(today, terms, privacies):
    answer = []
    dic = {}
    ty, tm, td = map(int, today.split('.'))
    
    for t in terms:
        a,b = t.split()
        dic[a] = int(b)
        
    for idx,p in enumerate (privacies , start = 1):
        day,pri = p.split()
        y,m,d = map(int,day.split('.'))
        s = dic.get(pri)
        
        m = s+m
        
        if m > 12:
            while m > 12:
                y += 1
                m = m-12
        
        if d < 2:
            m -= 1
            if m == 0:
                m = 12
                y -= 1
            
            d = 28
        elif d >= 2:
            d -= 1
         
        if ty > y:
            answer.append(idx)
        elif ty == y :
            if tm > m:
                answer.append(idx)
            elif tm == m and td > d:
                answer.append(idx)
        
    return answer