m,n = map(int,input().split())
chess = [list(input()) for _ in range(m)]
min_cnt = 64

for i in range(m-7):
    for j in range(n-7):
    #     print(chess[x][y], end = ' ')
    # print()
        w_start = 0
        B_start = 0
        
        for x in range(8):
            for y in range(8):
                cur = chess[i+x][j+y]

                if (x + y) % 2 == 0:
                    if cur != 'W': w_start += 1
                    if cur != 'B': B_start += 1
                else:
                    if cur != 'B': w_start += 1
                    if cur != 'W': B_start += 1

        min_cnt = min(min_cnt, w_start, B_start)

print(min_cnt)
            
