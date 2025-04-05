import sys

input = sys.stdin.readline
T= int(input().strip()) 

for i in range(T):
    a,b = map(int,input().strip().split())
    print(a+b)