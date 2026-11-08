def solution(prices):
    answer = []
    idx = 0 # 현재 idx 
    idx2 = idx + 1 
    
    while idx < len(prices): # 바깥 while - 전체 prices 순회
        cnt = 0
        
        while idx2 < len(prices): # 내부 while - 상승되는 동안 순회
            cnt += 1
            
            if prices[idx] <= prices[idx2]:
                idx2 += 1
            else:
                # 가격 떨어지면 idx 한 칸 옮긴 후, idx2도 idx에 초기화
                break
        idx += 1            
        idx2 = idx + 1
                
        answer.append(cnt)
                
    return answer  