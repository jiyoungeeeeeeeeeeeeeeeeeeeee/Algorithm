import sys

n = int(sys.stdin.readline())

for i in range(1,n+1):
    word = sys.stdin.readline().split()
    print(f"Case #{i}:" ,*word[::-1])