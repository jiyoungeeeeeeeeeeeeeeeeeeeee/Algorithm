def solution(n):
    lst = []
    for o in str(n):
        lst.append(o)
    lst.sort(reverse = True)
    return int(''.join(lst))