def solution(s):
    answer = []
    save   = [] 
    idx    = 0
    
    while idx < len(s):
        idx2 = idx - 1
        cnt  = 1
        if s[idx] in save:
                while idx2 >= 0:
                    if s[idx2] == s[idx]:
                        answer.append(cnt)
                        idx += 1
                        break
                        
                    else:
                        idx2 -= 1
                        cnt += 1
                
        else:
            answer.append(-1)
            save.append(s[idx])
            idx += 1
    
    return answer