# 열의 개수는 미지수 => 가장 긴 열의 길이로 맞춰줌 
n = 5
arr = [list(map(str,input())) for _ in range(n)]

max_row = max(len(row) for row in arr)

for j in range(max_row): #열
    for i in range(n): #행
        if j < len(arr[i]):
            print(arr[i][j], end = '')
