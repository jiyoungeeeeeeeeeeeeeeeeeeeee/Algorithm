def solution(A, B):
    cnt = 0
    
    if A == B:
        return 0
    
    state = False
    
    push = A
    
    while cnt < len(A):
        cnt += 1
        end =  push[-1] 
        push = end + push[:len(A)-1]
        
        if push == B:
            state = True
            return cnt
        else:
            push = push
    
    if state == False:
        return -1    
        return push