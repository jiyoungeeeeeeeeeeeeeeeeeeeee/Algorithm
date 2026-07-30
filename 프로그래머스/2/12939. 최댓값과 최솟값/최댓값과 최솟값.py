def solution(s):
    answer = ''
    num = list(map(int, s.split()))
    M,m = max(num),min(num)
    return f"{m} {M}"
