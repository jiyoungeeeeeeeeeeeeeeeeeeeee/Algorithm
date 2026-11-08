def solution(prices):
    answer = []
    idx = 0
    
    while idx < len(prices):
        cnt = 0
        idx2 = idx+1
            
        while idx2 < len(prices): 
            cnt += 1
            if prices[idx] <= prices[idx2]:
                idx2 += 1      

            else:
                break # 내부 while 바로 종료 후 아래 바깥 while문에서 저장
                
                
        # idx부터 끝까지 전부 idx보다 같거나 큰 경우 저장하기
        answer.append(cnt)
        idx += 1
        


    return answer 