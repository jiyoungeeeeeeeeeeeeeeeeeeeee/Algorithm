import sys
n = int(sys.stdin.readline())

for i in range(n):
    passward = sys.stdin.readline().strip()
    lengh = len(passward)

    if lengh >= 6 and lengh <= 9:
        print('yes')
    else:
        print('no')    