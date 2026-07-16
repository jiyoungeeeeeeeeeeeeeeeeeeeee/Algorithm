def solution(people, limit):
    cnt = 0
    people.sort()
    r = len(people) - 1
    l = 0
    
    while l <= r:
        if people[r] + people[l] <= limit:
            cnt += 1
            r -= 1
            l += 1
        else:
            cnt += 1
            r -= 1
    
    return cnt