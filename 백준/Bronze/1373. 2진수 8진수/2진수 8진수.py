import sys

binary = list(map(int,sys.stdin.readline().strip()))
groups = []

while len(binary)%3 != 0:
    binary.insert(0,0)

for i in range(0,len(binary),3):
    groups.append(binary[i:i+3])

for group in groups:
    a,b,c = group
    value = a*4 + b*2 + c*1
    print(value, end = '')