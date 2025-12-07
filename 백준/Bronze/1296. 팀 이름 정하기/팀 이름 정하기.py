import sys

yeondu = sys.stdin.readline().strip()
n = int(sys.stdin.readline())

def calculation(du , win):
    name = du + win
    l = name.count('L')
    o = name.count('O')
    v = name.count('V')
    e = name.count('E')

    score = ((l+o) * (l+v) * (l+e) * (o+v) * (o+e) * (v+e)) % 100
    return score

result = []

for _ in range(n):
    team = sys.stdin.readline().strip()
    result.append((calculation(yeondu,team),team))
result.sort(key = lambda x: (-x[0] , x[1]))    
print(result[0][1])  
    