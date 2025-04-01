n, m = map(int, input().split())

# 행렬 A 입력 받기
A = [list(map(int, input().split())) for _ in range(n)]

# 행렬 B 입력 받기
B = [list(map(int, input().split())) for _ in range(n)]

# 결과 행렬 생성
result = [[0] * m for _ in range(n)]

# 행렬 덧셈 수행
for i in range(n):
    for j in range(m):
        result[i][j] = A[i][j] + B[i][j]

# 결과 출력
for row in result:
    print(*row)
