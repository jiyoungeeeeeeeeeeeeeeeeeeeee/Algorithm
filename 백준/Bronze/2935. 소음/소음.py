import sys
a = int(sys.stdin.readline())
operator = sys.stdin.readline().strip()
b = int(sys.stdin.readline())


if operator == '+':
    print(a+b)
    
elif operator == '*':
    print(a*b)
