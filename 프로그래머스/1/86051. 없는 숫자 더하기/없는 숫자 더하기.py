def solution(numbers):
    answer = -1
    s = set(numbers)
    o = set(range(10))
    result = o-s
    return sum(result)