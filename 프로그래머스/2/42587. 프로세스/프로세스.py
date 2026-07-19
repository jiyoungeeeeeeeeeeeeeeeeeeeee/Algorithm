from collections import deque

def solution(priorities, location):
    answer = 0
    dp = deque()
    
    for i in range(len(priorities)):
        dp.append((priorities[i],i)) # (우선순위,인덱스)
    
    while dp:
        s = dp.popleft()
        if any(s[0] < process[0] for process in dp):
            dp.append(s)
        else:   
            answer += 1
            
            if s[1] == location:
                return answer