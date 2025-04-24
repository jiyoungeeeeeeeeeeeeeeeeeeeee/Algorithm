n = int(input())
x_list=[]
y_list=[]

for i in range(n):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)


width  = max(x_list) - min(x_list) 
length = max(y_list) - min(y_list) 

print(width*length)

