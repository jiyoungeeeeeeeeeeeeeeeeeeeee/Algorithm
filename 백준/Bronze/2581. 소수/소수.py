m = int(input())
n = int(input())
num_list = []

for i in range(m,n+1):
    if i < 2:
        continue
    
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        num_list.append(i)
        
if num_list:        
    print(sum(num_list))
    print(min(num_list))
else :
    print(-1)