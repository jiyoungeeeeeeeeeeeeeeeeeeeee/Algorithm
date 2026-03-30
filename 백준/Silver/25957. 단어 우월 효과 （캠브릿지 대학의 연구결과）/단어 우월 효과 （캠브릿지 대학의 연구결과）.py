import sys

n = int(sys.stdin.readline())

dic = {}

for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) == 1:
        dic[word[0]] = word
    else:
        s = sorted(word[1:-1])
        wsw = word[0], ''.join(s),word[-1]    
        dic[wsw] = word


m = int(sys.stdin.readline())
text = sys.stdin.readline().split()

for t in text:
    if len(t) == 1:
        print(dic[t[0]], end = ' ')
    else:
        a = sorted(t[1:-1])
        tat = t[0], ''.join(a),t[-1]    
        
        print(dic[tat] , end = ' ')
