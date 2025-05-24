import sys

while True:
    line  = sys.stdin.readline().rstrip('\n')
    if not line:
        break

    upper = 0
    lower = 0
    num = 0
    gap = 0  
# 소문자, 대문자 , 숫자 , 공백의 개수 

    for i in line:
          
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            num += 1
        elif i.isspace():
            gap += 1

    print(lower,upper,num,gap)

    