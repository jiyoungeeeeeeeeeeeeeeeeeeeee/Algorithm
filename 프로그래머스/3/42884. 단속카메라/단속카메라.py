def solution(routes):
    routes.sort(key=lambda x: x[1])

    cnt = 0
    lst = []

    for t in routes:
        if not lst or t[0] > lst[-1]:
            lst.append(t[1])
            cnt += 1

    return cnt