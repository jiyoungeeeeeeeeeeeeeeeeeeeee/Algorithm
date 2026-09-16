def solution(d, budget):
    total = 0
    cnt = 0
    
    d.sort()
    
    for D in d:
        total += D
        if total <= budget:
            cnt += 1
        elif total > budget:
            break
    
    return cnt