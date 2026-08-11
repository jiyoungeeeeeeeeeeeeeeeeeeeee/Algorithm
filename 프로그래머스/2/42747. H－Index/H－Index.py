def solution(citations):
    answer = 0
    citations = sorted(citations)
    n = len(citations)
    
    for i,c in enumerate(citations):
        num = n - i
        if c >= num:
            answer = num
            
            return num
    
    return 0