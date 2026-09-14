def solution(n):
    idx = 1 
    cnt = 0

    while idx  <= n:
        total = 0   

        for i in range(idx , n+1):
            total += i
            
            if total > n:
                break
                
            elif total == n:
                cnt += 1
                break
                
        idx += 1
            
    return cnt 