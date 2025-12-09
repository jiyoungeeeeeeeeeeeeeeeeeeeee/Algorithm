import sys

lst = []
while True:
    puzzle = sys.stdin.readline().strip()
    if puzzle == 'END':
        break
    lst.append(puzzle)


for i in range(0,len(lst),2):
    compate = lst[i:i+2]

    if sorted(compate[1]) == sorted(compate[0]):

        print(f'Case {(i//2)+1}: same')
    else:
        print(f'Case {(i//2)+1}: different')