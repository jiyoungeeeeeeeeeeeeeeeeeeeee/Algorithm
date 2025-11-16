import sys
isbn = list(sys.stdin.readline().strip())
s = 0
star_weight = None

for i in range(len(isbn)):
    if (i+1) % 2 == 0:
        if isbn[i] == "*":
            star_weight = 3
        else:
            s += int(isbn[i]) * 3
    else:
        if isbn[i] == "*":
            star_weight = 1
        else:
            s += int(isbn[i]) * 1

if star_weight == 1:
    x = (10 - (s % 10)) % 10
else:  # star_weight == 3
    x = ((10 - (s % 10)) % 10) * 7 % 10

print(x)
