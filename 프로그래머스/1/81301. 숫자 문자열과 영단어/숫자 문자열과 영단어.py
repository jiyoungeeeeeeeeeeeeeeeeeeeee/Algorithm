def solution(s):
    ans = ''
    dic = { 'zero'  :'0',
            'one'   :'1',
            'two'   :'2',
            'three' :'3',
            'four'  :'4',
            'five'  :'5',
            'six'   :'6',
            'seven' :'7',
            'eight' :'8',
            'nine'  :'9'
         }
    text = ''

    for o in s:
        
        if o.isdigit():
            # lst.append(o)
            ans += o
        else:
            text += o
        
        if text not in dic:
            continue
        else:
            c = dic[text]
            # lst.append(c)
            ans += c
            text = ''

    return int(ans)