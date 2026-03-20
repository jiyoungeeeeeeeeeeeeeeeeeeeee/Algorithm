import sys

n = int(sys.stdin.readline())
c = int(sys.stdin.readline())
dic = dict()

for _ in range(c):
    c1,c2 = map(int,sys.stdin.readline().split())
    
    if c1 not in dic:
        dic[c1] = []
    if c2 not in dic:
        dic[c2] = []

    dic[c1].append(c2)
    dic[c2].append(c1)

one = dic.get(1)    
result = set()

visited = set()
stack = [1]

while stack:
    now = stack.pop()

    if now not in visited:
        visited.add(now)

        for next_node in dic.get(now, []):
            if next_node not in visited:
                stack.append(next_node)

print(len(visited) - 1)
    