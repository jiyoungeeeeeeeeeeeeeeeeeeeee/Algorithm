def solution(sizes):
    answer = 0
    row = []
    col = []
    
    for s in sizes:
        w,h = s[0],s[1]

        M = max(w,h)
        m = min(w,h)
        row.append(M)
        col.append(m)
        
        
    return max(row) * max(col)