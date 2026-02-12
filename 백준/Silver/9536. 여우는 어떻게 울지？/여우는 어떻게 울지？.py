import sys

n = int(sys.stdin.readline())

for i in range(n):
    record = sys.stdin.readline().split()
    remove_set = set()

    while True:
        howling = sys.stdin.readline().rstrip()
        
        if howling[0] == 'w':
            break
        
        h = howling.split('goes')
        others = str(h[1].strip())
        remove_set.add(others)
    

    result = []
    for r in record:
        if r not in remove_set:
            result.append(r)
    
    print(*result)