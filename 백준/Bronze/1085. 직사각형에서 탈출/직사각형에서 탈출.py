x,y,w,h = list(map(int,input().split()))
# print(x,y,w,h)

line = []

lift = x
right = w-x
under = y
upper = h-y

line.extend([lift,right,under,upper])
print(min(line))
