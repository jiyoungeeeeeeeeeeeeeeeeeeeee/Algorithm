import sys
cnt = 0

for i in range(8):
    chess = sys.stdin.readline().strip()

    if i%2 == 0:
        white = chess[::2]  

    else:
        white = chess[1::2]
    
    for ch in white:
        if ch == "F":
            cnt += 1

print(cnt)
    
