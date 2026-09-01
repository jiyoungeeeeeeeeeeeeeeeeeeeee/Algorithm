def solution(absolutes, signs):
    answer = 123456789
    sol = 0
    for i in range(len(signs)):
        if signs[i] == True:
            sol += absolutes[i]
        else:
            sol -= absolutes[i]
    return sol