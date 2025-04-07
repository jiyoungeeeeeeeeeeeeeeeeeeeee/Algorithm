n = int(input())
scores = list(map(int,input().split()))

m = max(scores)

new_score = 0

for score in scores:
    new_score += score/m*100
    
average = new_score/n

print(average)