def solution(food):
    answer = ''
    water = food[0]
    
    for i in range(1,len(food)):
        while food[i] > 1 :
            food[i] -= 2
            answer += str(i)
        
    return answer +'0'+answer[::-1]