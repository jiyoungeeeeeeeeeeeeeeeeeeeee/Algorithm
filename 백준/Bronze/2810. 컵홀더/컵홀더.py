import sys

n = int(sys.stdin.readline())
seat = sys.stdin.readline().strip()

cl = seat.count('LL')
cs = seat.count('S')

if cl == 0:
    print(cs)
else:
    print(cl+cs+1)