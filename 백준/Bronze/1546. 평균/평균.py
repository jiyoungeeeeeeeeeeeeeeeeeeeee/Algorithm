n = int(input())
scores = list(map(int,input().split()))

max_score = scores[0]

for score in scores:
    if score > max_score:
        max_score = score

new_sum = 0

for score in scores:
    new_sum += (score/max_score*100)

average = new_sum/n
print(average)
