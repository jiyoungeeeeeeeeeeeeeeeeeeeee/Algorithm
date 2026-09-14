def solution(n):
    
    left = 1
    right = 1
    total = 1
    cnt = 0

    while left <= n and right <= n:

        if total == n :
            cnt += 1
            total -= left
            left += 1
        
        elif total < n :
            right += 1
            total += right
            
        else:
            total -= left
            left += 1
            
    return cnt