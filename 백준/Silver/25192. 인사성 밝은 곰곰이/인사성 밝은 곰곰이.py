import sys
from collections import Counter

n = int(sys.stdin.readline())
lst = set()
cnt = 0

for i in range(n):
    nickname = sys.stdin.readline().strip()
    
    if nickname == 'ENTER':
        lst.clear()
        continue
    else:        
        if nickname in lst:
            continue
        else:
            cnt += 1
            lst.add(nickname)

print(cnt)