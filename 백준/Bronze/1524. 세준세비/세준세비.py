import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):

    line = input().strip()
    
    while line == '':
        line = input().strip()   

    n, m = map(int, line.split())
    sejun = list(map(int, input().split()))
    sebi = list(map(int, input().split()))

    if max(sejun) >= max(sebi):
        print('S')
    else:
        print('B')