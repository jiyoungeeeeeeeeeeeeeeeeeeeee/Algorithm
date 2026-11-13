def solution(A, B):
    cnt = 0
    
    if A == B:
        return 0
        
    push = A
    
    while cnt < len(A):
        cnt += 1
        end =  push[-1] 
        push = end + push[:len(A)-1]
        
        if push == B:
            return cnt
        else:
            push = push
    
    return -1
