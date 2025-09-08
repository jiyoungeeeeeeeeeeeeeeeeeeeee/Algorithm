import sys
k = int(sys.stdin.readline())

lst = []

for i in range(k):
    jeamin = int(sys.stdin.readline())

    if jeamin != 0:
        lst.append(jeamin)
    else:
        lst.pop()
print(sum(lst))