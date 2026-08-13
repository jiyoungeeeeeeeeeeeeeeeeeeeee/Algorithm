def solution(s):
    answer = True
    s = s.lower()
    cnt_p = s.count('p')
    cnt_y = s.count('y')
    
    if cnt_p == 0 and cnt_y == 0:
        return True
    else:
        if cnt_p == cnt_y:
            return True

        return False