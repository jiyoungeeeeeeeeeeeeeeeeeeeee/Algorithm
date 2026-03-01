import sys

t = int(sys.stdin.readline())

for _ in range(t): 
    s,p = sys.stdin.readline().split()    
    i = 0
    cnt = 0

    while i < len(s):

        if s[i:len(p)+i] == p:
            cnt += 1
            i += len(p)
        else:

            i += 1

    print(cnt + (len(s) - cnt * len(p)))