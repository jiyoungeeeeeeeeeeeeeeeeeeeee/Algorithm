def solution(S):
    same = 0
    diff = 0    
    x = ''
    cnt = 0
    
    for s in S:
        if same == 0 and diff == 0:
            x = s
            
        if s == x:
            same += 1
        else:
            diff += 1
        
        if same == diff:
            cnt += 1
            same = 0
            diff = 0
    
    if same != 0 or diff != 0:
        cnt += 1
    
    return cnt