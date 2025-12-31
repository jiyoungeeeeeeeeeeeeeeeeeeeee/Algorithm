import sys

n = int(sys.stdin.readline())
prize = []

for i in range(n):
    dice = list(map(int,sys.stdin.readline().split()))
    
    if dice[0] == dice[1] == dice[2]:
        a = 10_000 + dice[0] * 1_000
        prize.append(a)
    elif dice[0] != dice[1] and dice[1] != dice[2] and dice[0] != dice[2]:
        c = max(dice) * 100
        prize.append(c)
    else:
        if dice.count(min(dice)) == 2:
            b = 1000 + min(dice)*100
            prize.append(b)

        elif dice.count(max(dice)) == 2:
            e = 1000 + max(dice)*100
            prize.append(e)

print(max(prize))
