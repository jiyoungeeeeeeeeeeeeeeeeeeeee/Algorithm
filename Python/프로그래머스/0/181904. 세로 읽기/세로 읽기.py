def solution(my_string, m, c):
    answer = ''
    
    num = len(my_string)//m
    idx = 0
    for _ in range(num):
        answer += my_string[idx:idx+m][c-1]
        idx += m
    return answer