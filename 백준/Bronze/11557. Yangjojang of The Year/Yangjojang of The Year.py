import sys
T = int(sys.stdin.readline())

for t in range(T):
    n = int(sys.stdin.readline())
    items = []
    for i in range(n):
        s , l = sys.stdin.readline().split()
        items.append((s,int(l)))
    
        items.sort(key=lambda x: x[1] , reverse = True)
    print(items[0][0])        