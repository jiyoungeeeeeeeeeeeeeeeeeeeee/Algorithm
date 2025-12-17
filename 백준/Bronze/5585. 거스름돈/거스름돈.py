import sys

pay = 1000
money = int(sys.stdin.readline())
cnt = 0

change = pay - money

for coin in [500,100,50,10,5,1]:
    while change >= coin:
        change -= coin
        cnt += 1
print(cnt)
