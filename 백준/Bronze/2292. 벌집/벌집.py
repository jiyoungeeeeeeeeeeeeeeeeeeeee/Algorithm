n = int(input())

floor = 1
honeycomb_cnt = 1

while n >honeycomb_cnt:

    honeycomb_cnt += floor*6
    floor += 1 

print(floor)