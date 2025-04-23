x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())
x3, y3 = map(int,input().split())

x_list = []
y_list = []

x_list.extend([x1,x2,x3])
y_list.extend([y1,y2,y3])

x4 = [x for x in x_list if x_list.count(x) == 1]
y4 = [y for y in y_list if y_list.count(y) == 1]

print(*x4,*y4)