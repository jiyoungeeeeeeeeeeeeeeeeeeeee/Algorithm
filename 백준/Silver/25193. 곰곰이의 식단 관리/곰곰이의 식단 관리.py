import sys

n = int(sys.stdin.readline())
day = sys.stdin.readline().strip()

c = day.count('C')
other = n - c
slots = other + 1

print((c + slots - 1) // slots)