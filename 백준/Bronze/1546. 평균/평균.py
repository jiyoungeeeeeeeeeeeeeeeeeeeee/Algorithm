n = int(input())
scores = list(map(int,input().split()))

m = max(scores)

new_scores = [score/m*100 for score in scores]

average = sum(new_scores)/n

print(average)