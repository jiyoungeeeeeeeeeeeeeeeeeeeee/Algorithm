import sys

t = int(sys.stdin.readline())

for _ in range(t): 
    s,p = sys.stdin.readline().split()    

    cnt = s.count(p)
    print(len(s) - cnt * len(p) + cnt)