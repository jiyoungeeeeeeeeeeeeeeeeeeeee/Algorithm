def solution(X,Y):
    i = 0
    j = 0
    result = ''
    x = sorted(X)
    y = sorted(Y)
    
    while len(x) > i and len(y) > j:
        if x[i] == y[j]:
            result += x[i]
            i += 1
            j += 1
        elif x[i] < y[j]:
            i += 1
        else:
            j += 1
        
    if result == '':
        return '-1'

    if set(result) == {'0'}:
        return '0'

    return ''.join(sorted(result, reverse=True))


