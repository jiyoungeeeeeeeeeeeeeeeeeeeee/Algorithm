import sys
n = int(sys.stdin.readline())
treasure = list(map(int,sys.stdin.readline().split()))
treasure.sort(reverse = True)

print(sum(treasure[:n//2]))