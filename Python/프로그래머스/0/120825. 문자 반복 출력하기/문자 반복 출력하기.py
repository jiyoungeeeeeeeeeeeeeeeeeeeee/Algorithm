def solution(my_string, n):
    answer = ''
    idx = 0
    while idx < len(my_string):
        for i in range(n):
            answer += my_string[idx] 
        idx += 1 
    
    return answer