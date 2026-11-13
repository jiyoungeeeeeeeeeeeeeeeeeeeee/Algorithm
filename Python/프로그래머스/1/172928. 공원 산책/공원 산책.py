def solution(park, routes):
    answer = []
    
    for p in range(len(park)): # row
        for q in range(len(park[0])): # column
            
            if park[p][q] == 'S':
                Srow,Scol = p,q # 시작 좌표
                break
            
            
    # 방해물이 없다면 -> 좌표 옮기기 , 실패하면 continue
    for r in routes:
        idx,i = r.split()
        i = int(i) 
        
        if idx == 'W':
            if Scol-i >= 0 and 'X' not in park[Srow][Scol-i:Scol+1] :# West
                Scol = Scol-i
            else:
                continue
        elif idx == 'E': # East
            if Scol+i < len(park[0]) and 'X' not in park[Srow][Scol:Scol+i+1] :
                Scol= Scol + i
            else:
                continue
        
        # while문으로 수정 
        elif idx == 'N':
            if Srow-i >= 0:
                state = True # 사용 가능 
                for s in range(i+1):
                    if 'X' in park[Srow-s][Scol]:  # North 
                        state = False
                        break
                if state == True:
                    Srow = Srow - i
                 
            else:
                continue
                
        elif idx == 'S':
            if Srow+i < len(park):
                state = True
                for s in range(i+1):
                    if 'X' in park[Srow+s][Scol]: # South
                        state = False
                        break 
                if state == True:
                    Srow = Srow + i
                
            else:
                continue
        
    
    return Srow,Scol