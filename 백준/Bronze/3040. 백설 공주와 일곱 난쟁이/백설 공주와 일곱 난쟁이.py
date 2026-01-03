import sys

lst = []
for i in range(9):
    num = int(sys.stdin.readline().strip())
    lst.append(num)

total = sum(lst)

for i in range(len(lst)):
    for j in range(i):
        if total - (lst[i] + lst[j]) == 100:
                a,b = lst[i],lst[j]
lst.remove(a)
lst.remove(b)

print(*lst , sep= '\n')