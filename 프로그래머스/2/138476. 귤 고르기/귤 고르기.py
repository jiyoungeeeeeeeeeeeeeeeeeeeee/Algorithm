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
        answer += 1

        if i < k:
            idx += 1
        else:
            return answer
    
    return answer