def solution(arr1, arr2):
    answer = []
    
    for a1,a2 in zip(arr1,arr2):
        row = []
        for n1,n2 in zip(a1,a2):
            row.append(n1+n2)
        answer.append(row)
    return answer