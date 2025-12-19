import sys

n,m = map(int,sys.stdin.readline().split())
s = sys.stdin.readline().strip()

for i in range(m):
    postit = sys.stdin.readline().strip()
    idx = 0

    if len(postit) >= len(s):

        for p in postit:
            if idx < len(s) and p == s[idx]:
                idx += 1
        if idx == len(s):
            print('true')
        else:
            print('false')

    else:
        print('false')