import sys
cnt1 = 0
cnt2 = 0

for i in range(8):
    chess = sys.stdin.readline().strip()
    if i == 0 or i%2 == 0:
        white1 = chess[::2]  
        for w1 in white1:
            if w1 == "F":
                cnt1 += 1

    else:
        white2 = chess[1::2]
        for w2 in white2:
            if w2 == "F":
                cnt2 += 1

print(cnt1+cnt2)
    
