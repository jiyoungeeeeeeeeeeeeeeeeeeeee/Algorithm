import sys
T = int(sys.stdin.readline())
score = list(map(int,sys.stdin.readline().split()))

while len(score) < 5:
    score.append(0)

if score[0] > score[2]:
    first = (score[0] - score[2])*508
elif score[0] <= score[2]:
    first = abs(score[0] - score[2])* 108

if score[1] > score[3]:
    second = (score[1] - score[3]) * 212
elif score[1] <= score[3]:
    second = abs(score[1] - score[3]) * 305

thrid = score[-1] * 707

print((first + second + thrid)*4763)
