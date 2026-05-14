def solution(schedules, timelogs, startday):
    
    answer = 0
    
    for i in range(len(schedules)):
        ok = True

        time = schedules[i]
        hour = time // 100
        minute = time % 100
        approve = hour * 60 + minute + 10  
        
        for day_idx, log in enumerate(timelogs[i]): 
            day = (startday + day_idx - 1) % 7 + 1
            log_hour = log // 100
            log_minute = log % 100
            log_time = log_hour * 60 + log_minute
            
            
            if day >= 6:
                continue
            
            elif day <= 5 and approve < log_time:
                ok = False
                break
            
        if ok:
            answer += 1
        
    return answer