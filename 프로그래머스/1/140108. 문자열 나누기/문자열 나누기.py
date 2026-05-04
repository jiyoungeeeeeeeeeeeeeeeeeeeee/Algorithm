def solution(S):
    cnt1 = 0
    cnt2 = 0    
    result = ''
    save = []
    x = ''
    
    for s in S:
        if x == '':
            x = s
            
        if s == x:
            cnt1 += 1
        else:
            cnt2 += 1
        
        result += s
        
        if cnt1 == cnt2:
            x = ''
            cnt1 = 0
            cnt2 = 0
            save.append(result)
            result = ''
        
    if result != '':
        save.append(result)

    return len(save)