import sys
n,m = map(int,sys.stdin.readline().split())
lst = []

for i in range(m):
    a = list(map(int,sys.stdin.readline().rstrip().split()))
    lst.append((a,i))

lst.sort()
result = []
y_end = []
num = 1

for j in range(m):
    if  num == lst[j][0][0]:

        if not y_end:
            y_end.append(lst[j][0][2])
            result.append(('YES',lst[j][1]))

        elif y_end[-1] <= lst[j][0][1]:
            result.append(('YES',lst[j][1]))
            y_end.append(lst[j][0][2])
    
        elif y_end[-1] > lst[j][0][1]: 
            result.append(('NO', lst[j][1]))


    elif num < lst[j][0][0]:

        y_end.clear()
        num = lst[j][0][0]

        if not y_end:
            y_end.append(lst[j][0][2])
            result.append(('YES',lst[j][1]))

        elif y_end[-1] <= lst[j][0][1]:
            result.append(('YES',lst[j][1]))
            y_end.append(lst[j][0][2])
    
        elif y_end[-1] > lst[j][0][1]: 
            result.append(('NO', lst[j][1]))

result.sort(key = lambda x:x[1])
for r in result:
    print(r[0])