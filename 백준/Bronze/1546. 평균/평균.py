n = int(input())
scores = list(map(int,input().split()))
re_score = 0
max_scores = max(scores) 

for s in scores:
    re_score += s/max_scores*100
    

print(re_score/n)
    