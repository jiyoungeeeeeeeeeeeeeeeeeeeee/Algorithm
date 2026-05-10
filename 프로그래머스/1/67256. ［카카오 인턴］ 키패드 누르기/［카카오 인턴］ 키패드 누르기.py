def solution(numbers, hand):
    answer = ''
    lp = (0,3) 
    rp = (2,3)
    pos = {
        1: (0, 0), 2: (1, 0), 3: (2, 0),
        4: (0, 1), 5: (1, 1), 6: (2, 1),
        7: (0, 2), 8: (1, 2), 9: (2, 2),
        0: (1, 3)
    }
    if hand == "right":
        hand = 'R'
    elif hand == 'left':
        hand = 'L'
    
    for n in numbers:
        target = pos[n]
        
        if n in [1,4,7]:
            answer += 'L'
            lp = target
                
        elif n in [3,6,9]:
            answer += 'R'
            rp = target
        
        else:
            ld = abs(lp[0] - target[0]) + abs(lp[1] - target[1])
            rd = abs(rp[0] - target[0]) + abs(rp[1] - target[1])
            
            if rd > ld:
                answer += 'L'
                lp = target
            elif rd < ld:
                answer += 'R'
                rp = target
            else:
                answer += hand
                
                if hand == 'L':
                    lp = target
                else:
                    rp = target
    return answer