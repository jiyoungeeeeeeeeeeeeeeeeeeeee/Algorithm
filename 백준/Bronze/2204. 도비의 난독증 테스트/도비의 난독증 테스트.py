import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    arr = []
    for i in range(n):
        word = sys.stdin.readline().strip()
        arr.append(word)
    
    arr.sort(key = str.lower)
    print(arr[0])
