e,s,m = map(int,input().split())
year = e

while True:
    if (year - 1) % 28 + 1 == s and (year - 1) % 19 + 1 == m:
        print(year)
        break
    else:
        year += 15
