def solution(arr):
    if len(arr) >= 2 :
        m = min(arr)
        while m in arr:
            arr.remove(m)
        return arr
    else:
        return [-1]
    
        