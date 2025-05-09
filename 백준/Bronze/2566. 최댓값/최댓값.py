numbers = [list(map(int,input().split())) for _ in range(9)]
max_pos = numbers[0][0]
m_num = -1
for i in range(9):
    for j in range(9):
        if m_num < numbers[i][j]:
            m_num = numbers[i][j]
            max_pos = (i,j)
        

print(m_num)
print(max_pos[0] + 1, max_pos[1] + 1)