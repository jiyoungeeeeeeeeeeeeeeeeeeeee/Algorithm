from collections import Counter
def solution(strings, n):
    answer = []
    
    s = sorted(strings, key = lambda x: (x[n],x))

    return s