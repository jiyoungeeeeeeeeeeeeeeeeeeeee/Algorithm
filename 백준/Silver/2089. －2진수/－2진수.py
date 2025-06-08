import sys

n = int(sys.stdin.readline())
result = []

if n == 0:
    print(0)
    sys.exit()

while n != 0:
    quo , remain = divmod(n , -2)    
    
    if remain < 0 :
        remain += 2
        quo += 1
    
    n = quo
    result.append(str(remain))    

print(''.join(reversed(result)))

