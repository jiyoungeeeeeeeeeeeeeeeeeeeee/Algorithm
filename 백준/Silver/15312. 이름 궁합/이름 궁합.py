import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

dict_match = {
    'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2,
    'H': 3, 'I': 3, 'J': 2, 'K': 2, 'L': 1, 'M': 2, 'N': 2,
    'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1,
    'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1
}

naming = ''

for i in range(len(a)):
    naming += a[i]
    naming += b[i]

trans = []

for n in naming:
    t= dict_match[n]
    trans.append(t)

# print(trans)

while len(trans) > 2:

    cal = []
    for i in range(len(trans)-1):
        tt = trans[i] + trans[i+1]
        # print(tt , 'tt의 합 구하는 중')
        cal.append(tt%10)
        # print(cal, 'cal의 현재상태')
    trans = cal[:]

print(str(trans[0]) + str(trans[1]))
    
