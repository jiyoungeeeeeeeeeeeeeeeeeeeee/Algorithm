from collections import deque
two = deque(list(map(int,input())))

while len(two)%3 != 0:
    two.insert(0,0)

while two:
    save = []
    a = two.popleft()
    b = two.popleft()
    c = two.popleft()

    val = a*4 + b*2 + c*1
    print(val , end = '')
