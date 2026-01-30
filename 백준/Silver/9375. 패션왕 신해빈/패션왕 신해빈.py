import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a = int(sys.stdin.readline())
    dic = {}
    for _ in range(a):
        garments , category = sys.stdin.readline().rstrip().split()
        if category not in dic:
            dic[category] = 1
        else:
            dic[category] += 1

    ans = 1
    for v in dic.values():
        ans *= (v+1)
    print(ans - 1)