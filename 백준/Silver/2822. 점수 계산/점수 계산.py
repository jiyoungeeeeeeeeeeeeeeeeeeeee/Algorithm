import sys
lst = []
for _ in range(8):
    score = int(sys.stdin.readline())
    lst.append(score)

items = []
for value,index in enumerate(lst, start=1):
    items.append((index,value))
items.sort(reverse = True)

result = []
total = []
for v,i in items:
    result.append(i)
    total.append(v)
    
print(sum(total[:5]))
print(*sorted(result[:5]))