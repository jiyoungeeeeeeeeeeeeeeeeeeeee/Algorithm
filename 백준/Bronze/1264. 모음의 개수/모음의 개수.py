import sys

while True:
    text = sys.stdin.readline().strip()
    if text == '#':
        break
    
    cnt = 0

    for t in text:
        if t in 'aeiouAEIOU':
            cnt += 1
    print(cnt)