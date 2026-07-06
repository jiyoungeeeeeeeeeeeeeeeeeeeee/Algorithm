from collections import Counter

def solution(k, tangerine):
    c = Counter(tangerine)    
    cnt = list(c.values())   
    cnt.sort(reverse = True)
    i = 0
    idx = 0
    answer = 0
    
    while k > i :
        i += cnt[idx]
        if i < k:
            idx += 1
            answer += 1
        else:
            answer += 1
            return answer
    
    return answer