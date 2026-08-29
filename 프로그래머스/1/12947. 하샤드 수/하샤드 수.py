def solution(x):
    X = x
    answer = 0
    
    while x > 0:
        answer += x % 10
        x //= 10
    
    return X%answer == 0