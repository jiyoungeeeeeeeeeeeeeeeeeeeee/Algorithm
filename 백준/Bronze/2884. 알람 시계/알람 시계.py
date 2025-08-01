h , m = map(int,input().split())

mh = h*60
all_time = mh + m

alarm = all_time - 45

if alarm < 0:
    alarm += 24*60

hour = alarm // 60
minute = alarm % 60

print(hour, minute)
