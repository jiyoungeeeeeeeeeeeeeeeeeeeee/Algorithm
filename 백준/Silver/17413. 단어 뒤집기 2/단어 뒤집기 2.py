import sys

s = sys.stdin.readline().strip()
stack = []
in_tag = False

for i in s:
    if i == "<":
        while stack:
            print(stack.pop(), end = '')
        in_tag = True
        print('<', end = '')
    
    elif i == ">":
        in_tag = False
        print(">", end = '')
    
    elif in_tag:
        print(i , end = '')
    
    elif i == ' ':
        while stack:
            print(stack.pop() , end = '')
        print(' ', end = '')
    
    else :
        stack.append(i)

while stack:
    print(stack.pop(), end = '')
            
        
