c = int(input())

for i in range(c):
    score = list(map(int,input().split()))
    students = score[0]
    scores = score[1:]
    total_score = sum(scores)

    means = int(total_score/students)
    
    # 비율
    cnt = 0
    for s in scores:
        if s > means:
            cnt += 1
    true = (cnt/students) * 100
    print(f"{true:.3f}%") 
