# 1 -> 1개 / 2 -> 6개 (2-7) / 3 -> 12개 (8-19) / 4 -> 18개(20-37)

n = int(input())

floor = 1
honeycomb_cnt = 1

while n > honeycomb_cnt:

    honeycomb_cnt += floor*6
    floor += 1 

print(floor)