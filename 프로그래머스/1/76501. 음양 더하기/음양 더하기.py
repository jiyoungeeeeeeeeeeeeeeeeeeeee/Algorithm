def solution(absolutes, signs):
    answer = 123456789
    sol = 0
    for a,s in zip(absolutes, signs):
        if s:
            sol += a
        else:
            sol -= a
    return sol