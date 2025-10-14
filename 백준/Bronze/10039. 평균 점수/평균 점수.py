import statistics
means = []

for _ in range(5):
    scores = int(input())

    if scores < 40:
        scores = 40
        means.append(scores)
    
    else :
        means.append(scores)
    
average = statistics.mean(means)
print(average)
        