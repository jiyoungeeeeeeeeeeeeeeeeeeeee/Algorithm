import sys

while True:
    lst = []
    drom = int(sys.stdin.readline())

    if drom == 0:
        break
    
    for i in str(drom):
        lst.append(i)
    
    reverse = lst[::-1]
    
    if lst == reverse :
        print('yes')
    else:
        print('no')            