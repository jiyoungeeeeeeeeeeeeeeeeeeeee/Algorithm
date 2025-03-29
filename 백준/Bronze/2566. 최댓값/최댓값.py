arr1 = [list(map(int,input().split())) for _ in range(9)]
max1 = arr1[0][0]
max_row, max_col = 0,0

for i in range(9):
    for j in range(9):
        if arr1[i][j] > max1:
            max1 = arr1[i][j]
            max_row , max_col = i,j
print(max1)
print(f"{max_row + 1} {max_col + 1}")
   
      