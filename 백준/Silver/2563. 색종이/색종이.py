# 0으로 채워진 배열 생성
# 이후 입력 n번만큼 x,y 받기
# 이중 for문에서 범위를 각 x,y에서 +10 만큼 1로 배열 바꾸기
# 1의 개수 세어주기 

n = int(input())
box = [list(0 for j in range(100)) for _ in range(100)]
cnt = 0

for i in range(n):
    x,y = map(int,input().split())

    for x_ext in range(x, x+10):
        for y_ext in range(y, y+10):
            box[x_ext][y_ext] = 1

for arr_row in box:
    cnt += arr_row.count(1)
print(cnt)
        