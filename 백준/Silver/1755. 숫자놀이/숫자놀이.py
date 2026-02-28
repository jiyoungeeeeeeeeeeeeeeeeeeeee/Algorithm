import sys

m,n = map(int,sys.stdin.readline().split())

nums = [i for i in range(m,n+1)]

dic = {0:'zero',1:'one', 2:'two', 3:'three', 4:'four', 5:'five',6:'six',7:'seven',8:'eight',     9:'nine'}
trans = []

for n in nums:
    if n >= 10:
        a,b = n//10 , n%10
        comb = dic.get(a)+ ' ' + dic.get(b)
        trans.append(comb)
    else:
        trans.append(dic.get(n))
trans.sort()

rev = {}
for k,v in dic.items():
    rev[v] = k

result = []
for t in trans:
    if len(t.split()) == 1:
        result.append(rev.get(t))
    else:
        a,b = t.split()
        A,B = rev.get(a) , rev.get(b)
        i = str(A)+str(B)
        result.append(i)

for j in range(((n-m)//10)+1):
    print(*result[j*10:10*(j+1)])
    
