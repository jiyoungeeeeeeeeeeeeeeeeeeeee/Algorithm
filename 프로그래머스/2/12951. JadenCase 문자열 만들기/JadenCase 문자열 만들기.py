def solution(s):
    answer = ''
    text = s.split(' ')
    lst = []
    
    for t in text:
        if t == '':
            lst.append('')
            continue
        
        t = t[0].upper() + t[1:].lower()
        lst.append(t)
        
    return ' '.join(lst) 