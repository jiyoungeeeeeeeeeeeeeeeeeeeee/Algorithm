def solution(a):
    idx = 0
    s = []
    for i in range(len(a)):
        s.append(a[i])
    x = s.copy()
    cnt = 0
    
    while idx < len(s):
        save = []
        state = True

        for i in range(len(a)):
            if x[i] == '[':
                save.append(x[i])
            elif x[i] == '(':
                save.append(x[i])
            elif x[i] == '{':
                save.append(x[i])
                
            elif x[i] == ']':
                if save and save[-1] == '[':
                    save.pop()
                else:
                    state = False
                    break
                    
            elif x[i] == ')':
                if save and save[-1] == '(':
                    save.pop()
                else:
                    state = False
                    break
            elif x[i] == '}':
                if save and save[-1] =='{':
                    save.pop() 
                else:
                    state = False
                    break
                    
        if state == True and not save:
            cnt += 1
            
        x = x[1:] + list(x[0])
        idx += 1
        
        
    return cnt