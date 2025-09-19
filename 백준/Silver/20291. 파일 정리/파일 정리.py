import sys
from collections import Counter ,defaultdict

n = int(input())
dic = defaultdict(int)

for i in range(n):
    files = input().strip()
    name , ext = files.split('.')

    dic[ext] += 1

for key in sorted(dic.keys()):
    print(key, dic[key])
    
