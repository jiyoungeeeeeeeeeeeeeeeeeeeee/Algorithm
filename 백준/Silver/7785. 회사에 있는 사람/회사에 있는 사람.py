import sys

n = int(sys.stdin.readline())

loglst = set()
for _ in range(n):
    name,log = sys.stdin.readline().split()

    if log == 'enter':
        loglst.add(name)
    if log == 'leave':
        loglst.remove(name)

lst = sorted(loglst, reverse = True)
print(*lst , sep = '\n')

