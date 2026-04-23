import sys

s = sys.stdin.readline().strip()
q = int(sys.stdin.readline())
lst = [ [0]*(len(s) + 1)   for i in range(26)]

for i in range(len(s)):
    for c in range(26):
        lst[c][i+1] = lst[c][i]
    
    idx = ord(s[i]) - ord ('a')
    lst[idx][i+1] += 1
  
answer = []
for _ in range(q):
    a,l,r = sys.stdin.readline().split()
    l,r = int(l),int(r)
    find = ord(a) - ord('a')
    result = lst[find][r+1] - lst[find][l]
    answer.append(result)

print(*answer , sep = '\n')