def solution(today, terms, privacies):
    answer = []
    dic = {}

    def to_days(date):
        y,m,d = map(int,date.split('.'))
        return y*12*28 + m*28 + d
    
    today_days = to_days(today)
    
    for t in terms:
        a,b = t.split()
        dic[a] = int(b)
        
    for idx,p in enumerate (privacies , start = 1):
        day,pri = p.split()
        
        start_day = to_days(day)
        i = dic.get(pri)
        
        if start_day + i *28 <= today_days:
            answer.append(idx)
        
    return answer