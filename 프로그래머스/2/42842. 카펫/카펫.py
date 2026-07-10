def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for i in range(2,total+1):
        if total%i == 0:
            b = total//i
            if b >= i:
                if (b - 2) * (i - 2) == yellow:
                    return [b, i]
         
    
