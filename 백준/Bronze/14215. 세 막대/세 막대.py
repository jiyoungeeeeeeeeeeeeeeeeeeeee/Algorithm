tri = []
a,b,c = map(int,input().split())

tri.extend([a,b,c])

max_side = max(tri)
total = a+b+c

if max_side < total - max_side:
    print(total)
else:
    print((total - max_side) + (total - max_side - 1))