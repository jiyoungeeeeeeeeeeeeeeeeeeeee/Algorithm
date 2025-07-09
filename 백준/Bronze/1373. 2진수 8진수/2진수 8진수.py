from collections import deque
two = deque(list(map(int,input())))

while len(two)%3 != 0:
    two.insert(0,0)
    
result = []

while two:
    a = two.pop()
    b = two.pop()
    c = two.pop()
    val = c*4 + b*2 + a*1
    result.append(val)

print(''.join(map(str, reversed(result))))

