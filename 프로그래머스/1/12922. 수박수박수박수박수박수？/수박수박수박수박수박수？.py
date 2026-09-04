def solution(n):
    answer = ''
    a = '수'
    b = '박'
    cnt = 0
    
    if n == 1:
        return a
    elif n == 2 :
        return a+b
    
    else:
        while cnt < n:
            answer += a
            cnt += 1
            
            if cnt < n:
                answer += b
                cnt += 1
        return answer