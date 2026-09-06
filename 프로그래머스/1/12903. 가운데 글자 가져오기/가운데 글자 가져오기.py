def solution(s):
    start = 0
    r = len(s)
    l = 0
    long = len(s)
    
    if len(s)%2 == 0:
        start = len(s)//2 
        return s[start-1] +s[start]
    else:
        while long > 1:
            r -= 1
            long -= 1
            
            if long > 1:
                l += 1
                long -= 1
        return s[l]