import sys

n = int(sys.stdin.readline())
lst = set()
cnt = 0

for i in range(n):
    nickname = sys.stdin.readline().strip()
    
    if nickname == 'ENTER':
        cnt += len(lst)
        lst.clear()
        continue
    else:        
        lst.add(nickname)
        
cnt += len(lst)
print(cnt)
