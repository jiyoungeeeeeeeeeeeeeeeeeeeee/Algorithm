def solution(new_id):
    answer = ''
    slist = ['~','!','@','#','$','%','^','&','*','(',')','=','+','[','{',']','}',':','?',',',"''",'<','>','/']
    one = new_id.lower()
    two = ''
    for t in one:
        if t in slist:
            continue
        else:
            two += t
    while '..' in two:
        two = two.replace('..','.')
    four = two.strip('.')
    
    if not four:
        four += 'a'
    
    six = four[:15]
    six = six.rstrip('.')
    
    if len(six) <= 2:
        last = six[-1]
        while len(six) < 3 :
            six += last
    
    return six