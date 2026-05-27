def solution(S):
    save = []
    for s in S:
        if s == '(':
            save.append(s)
        else:
            if save :
                save.pop()
            else:
                return False
    if save :
        return False
    else:
        return True

    # return 