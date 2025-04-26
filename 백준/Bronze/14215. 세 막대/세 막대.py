tri = sorted(map(int,input().split()))

max_side = tri[2] 
total = sum(tri)

if max_side < total - max_side:
    print(total)
else:
    print((total - max_side)*2- 1)