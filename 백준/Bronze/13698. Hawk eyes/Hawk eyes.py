import sys

sequence = sys.stdin.readline().strip()
cups = [i for i in range(1,5)]

small = cups[0]
big = cups[-1]


for s in sequence:
    if s == 'A':
        cups[0],cups[1] = cups[1],cups[0]
    elif s == 'B':
        cups[0],cups[2] = cups[2],cups[0]
    elif s == 'C':
        cups[0],cups[3] = cups[3],cups[0]
    elif s == 'D':
        cups[1],cups[2] = cups[2],cups[1]
    elif s == 'E':
        cups[1],cups[3] = cups[3],cups[1]
    elif s == 'F':
        cups[2],cups[3] = cups[3],cups[2]

print(cups.index(small)+1)
print(cups.index(big)+1)