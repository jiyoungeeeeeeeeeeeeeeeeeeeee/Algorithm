import sys

eight = list(map(int,sys.stdin.readline().split()))

ascend  = [i for i in range(1,9)]
descend = [i for i in range(8,0,-1)]

if eight == ascend:
    print('ascending')
elif eight == descend:
    print('descending')
else:
    print('mixed')