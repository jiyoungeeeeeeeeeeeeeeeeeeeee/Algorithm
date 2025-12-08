import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    lst = []
    orig = []
    for i in range(n):
        word = sys.stdin.readline().strip()
        orig.append(word)
        lst.append((word.lower(),i))
    lst.sort()
    grade = lst[0][1]                        
    print(orig[grade])
