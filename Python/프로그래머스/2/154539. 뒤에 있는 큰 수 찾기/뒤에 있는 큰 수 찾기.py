def solution(numbers):
    answer = [-1] * len(numbers)
    save = []

    for i in range(len(numbers)):
        while save and save[-1][1] < numbers[i]:
  
            idx,value = save.pop()
            answer[idx] = numbers[i]
        save.append((i,numbers[i]))
        
    return answer
