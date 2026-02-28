import sys

m,n = map(int,sys.stdin.readline().split())

nums = [i for i in range(m,n+1)]

dic = {0:'zero',1:'one', 2:'two', 3:'three', 4:'four', 5:'five',6:'six',7:'seven',8:'eight',     9:'nine'}

pair = []

for x in nums:
    if x >= 10:
        a,b = x//10 , x%10
        word = dic.get(a)+ ' ' + dic.get(b)
    else:
        word = dic.get(x)
    pair.append((word,x))
pair.sort()


cnt = 0
for word, x in pair:
    cnt += 1
    if cnt % 10 == 0:
        print(x)
    else:
        print(x, end=" ")
        
