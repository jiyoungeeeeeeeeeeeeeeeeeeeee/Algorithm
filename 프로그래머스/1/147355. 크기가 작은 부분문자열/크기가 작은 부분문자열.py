
def solution(t, p):
    idx = 0
    cnt = 0

    while idx < len(t) - len(p)+1:
        if int(t[idx:idx+len(p)]) <= int(p):
            cnt += 1
        idx += 1
    
    return cnt