import sys

while True:
    words = sys.stdin.readline().split()

    if not words :
        break

    s,t = words[0] , words[1]

    sp = 0
    tp = 0

    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
            sp += 1
        tp += 1
        
    if sp == len(s):
        print('Yes')
    else:
        print('No')
