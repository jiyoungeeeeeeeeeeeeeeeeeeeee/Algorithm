import sys
hwan = sys.stdin.readline().strip()
doctor = sys.stdin.readline().strip()

if len(hwan) >= len(doctor):
    print('go')
else:
    print('no')